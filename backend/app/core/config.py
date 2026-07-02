from pathlib import Path
from functools import lru_cache
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

_ENV_PATH = Path(__file__).resolve().parent.parent.parent / ".env"


class Settings(BaseSettings):

    # App details
    app_name: str = "PunchedN"
    app_description: str = (
        "API to assist with employee scheduling, and shift management."
    )
    app_version: str = "v1"
    app_docs_url: str = "/docs"
    app_redoc_url: str = "/redoc"
    admin_email: str
    debug: bool = False

    # Database settings
    mongo_db_user: str
    mongo_db_password: SecretStr
    mongo_db_host: str
    mongo_db_name: str

    @property
    def mongo_db_uri(self) -> str:
        return f"mongodb+srv://{self.mongo_db_user}:{self.mongo_db_password.get_secret_value()}@{self.mongo_db_host}/?appName={self.mongo_db_name}"

    # Load settings from .env
    model_config = SettingsConfigDict(env_file=_ENV_PATH)


# We are handling settings like this so we can test other settings via dependency injection.
# lru_cache will only create the settings object once, so there is not a constant need to read the .env file.
# https://fastapi.tiangolo.com/advanced/settings/?h=sett#creating-the-settings-only-once-with-lru-cache
@lru_cache
def get_settings() -> Settings:
    return Settings()
