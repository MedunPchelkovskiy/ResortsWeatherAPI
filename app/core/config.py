from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres-user:password@localhost:5432/raw_weather_api_data"

    tenant_id: str = ""
    client_id: str = ""
    client_secret: str = ""
    account_url: str = "https://etlflowrawdata.dfs.core.windows.net"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()