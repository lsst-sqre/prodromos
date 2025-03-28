"""Prodromos models."""

from pydantic import BaseModel


class SentryOrganization(BaseModel):
    """A Sentry Organization."""

    name: str


class SentryProject(BaseModel):
    """A Sentry project."""

    organization: SentryOrganization
    name: str


class SentryEnvironment(BaseModel):
    """A Sentry environment."""

    name: str


class SentryDsn(BaseModel):
    """A set of Sentry DSNs."""

    public: str
