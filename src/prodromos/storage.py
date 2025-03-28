from typing import Annotated

import httpx
from pydantic import BaseModel, Field

from .constants import SENTRY_BASE_URL, SENTRY_HTTP_TIMEOUT
from .exceptions import NoClientKeysError
from .models import SentryEnvironment, SentryProject


class SentryEnvironmentResponse(BaseModel):
    """An environment from the Sentry API."""

    name: str
    is_hidden: Annotated[bool, Field(alias="isHidden")]


class SentryDsnResponse(BaseModel):
    """A collection of DSNs from the Sentry API."""

    public: str


class SentryClientKeyResponse(BaseModel):
    """A client key from the Sentry API."""

    dsn: SentryDsnResponse


class SentryStorage:
    """Client for the Sentry HTTP API scoped to an organization and a project.

    https://docs.sentry.io/api/
    """

    def __init__(
        self,
        token: str,
        project: SentryProject,
        base_url: str = SENTRY_BASE_URL,
    ) -> None:
        self._project = project

        self._client = httpx.AsyncClient(
            base_url=f"{base_url}/projects/{project.organization.name}/{project.name}",
            follow_redirects=True,
            headers={"Authorization": f"Bearer {token}"},
            timeout=SENTRY_HTTP_TIMEOUT,
        )

    async def get_environment(
        self, environment: SentryEnvironment
    ) -> SentryEnvironmentResponse | None:
        """Get information about a Sentry environment.

        Parameters
        ----------
        environment
            The environment to look up

        Returns
        -------
        EnvironmentResponse | None
            Environment info, or None if the environment does not exist
        """
        res = await self._client.get("/environments")
        if res.status_code == 404:
            return None
        return SentryEnvironmentResponse.model_validate(res.json())

    async def get_keys(self) -> list[SentryClientKeyResponse]:
        """Get the first public DSN for this project."""
        res = self._client.get("/keys")
        keys = [
            SentryClientKeyResponse.model_validate(client_key.content)
            for client_key in res.json()
        ]
        if not keys:
            raise NoClientKeysError(self._project)
        return keys

    async def aclose(self) -> None:
        await self._client.aclose()
