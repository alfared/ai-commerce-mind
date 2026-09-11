from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Commerce Mind"
    app_env: str = "local"
    app_debug: bool = False
    app_version: str = "0.1.0"

    database_url: str = (
        "postgresql+asyncpg://ai_commerce_mind:ai_commerce_mind@localhost:5432/ai_commerce_mind"
    )

    redis_url: str = "redis://localhost:6379/0"

    openai_api_key: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
