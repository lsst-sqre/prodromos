"""Services to interact with Sentry."""

from .models import SentryEnvironment, SentryProject
from .storage import SentryStorage


class SentryService:
    """Project-scoped interactions with Sentry."""

    def __init__(self, token: str, project: SentryProject) -> None:
        self._storage = SentryStorage(token, project)

    async def create_environment(self, environment: SentryEnvironment) -> None:
        """Create a Sentry environment.

        Parameters
        ----------
        environment
            The sentry environment to create
        """
        # Check if the environment already exists
        if await self.get_environment(environment):
            return

        # An environment is implicitly created when Sentry ingests an event
        # tagged with that environment. There is no way to explicitly create an
        # environment:
        #
        # https://github.com/getsentry/sentry/issues/69546
        #
        # There is also no way to send an event through the HTTP API, so we
        # have to get a DSN via the HTTP API and then send an event with the
        # SDK.
        keys = await self._storage.get_keys()
        dsn = keys[0].dsn.public
        sdk_client = sentry_sdk.Client(dsn=dsn, environment=environment.name)
        sdk_client.capture_event(
            event={
                "message": f"Creating environment: {environment.name}",
                "level": "info",
            }
        )

        # This blocks the async event loop until our event is sent, but that's
        # fine
        sdk_client.close()
