from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings, loaded from environment variables / .env file.
    Copy .env.example to .env and adjust database_url for your local setup.
    """

    database_url: str = "postgresql+asyncpg://postgres-user:password@localhost:5432/raw_weather_api_data"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
