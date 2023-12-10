from functools import lru_cache

from pydantic import BaseModel, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresConfig(BaseModel):
    host: str = "localhost"
    port: int = 5432
    username: str = "postgres"
    db_name: str = "quickflow"

    def async_connector(self) -> str:
        return f"postgresql+asyncpg://{self.username}@{self.host}:{self.port}/{self.db_name}"

    def sync_connector(self) -> str:
        return f"postgresql://{self.username}@{self.host}:{self.port}/{self.db_name}"


class Settings(BaseSettings):
    database: PostgresConfig = PostgresConfig()
    cache: RedisDsn = "redis://localhost:6379/0"  # type: ignore

    model_config = SettingsConfigDict(env_file=".envrc")


@lru_cache
def get_settings() -> Settings:
    return Settings()
