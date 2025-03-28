from typing import Annotated
from pydantic_settings import BaseSettings
from pydantic import Field, SecretStr

class Config(BaseSettings):
    sentry_auth_token: Annotated[SecretStr, Field(title="Sentry auth token")]

config = Config()
