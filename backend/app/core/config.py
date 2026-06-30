from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PunchedN"
    admin_email: str


settings = Settings()
