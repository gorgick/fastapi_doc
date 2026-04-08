from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.second", ".env"),
    )
    host: str = "0.0.0.0"
    port: int = 8000
    url: PostgresDsn


settings = Settings()
