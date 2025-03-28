"""Prodromo exceptions."""

from .models import SentryProject


class NoClientKeysError(Exception):
    """No client keys (and thus no DSNs) found in a Sentry project.

    Parameters
    ----------
    project
        The Sentry project that was searched
    """

    def __init__(self, project: SentryProject) -> None:
        msg = (
            f"No DSNs found for project: {project.name} in organization:"
            f" {project.organization.name}"
        )
        super().__init__(msg)
