from functools import lru_cache
from typing import Optional, Dict, Any
from pydantic import BaseSettings, Field, PostgresDsn, validator


class Settings(BaseSettings):
    DB_NAME: str = Field(env='DB_NAME', default='postgres')
    DB_USER: str = Field(env='DB_USER', default='postgres')
    DB_PASS: str = Field(env='DB_PASSWORD', default='postgres')
    DB_HOST: str = Field(env='DB_HOST', default='localhost')
    DB_PORT: str = Field(env='DB_PORT', default='5432')
    DB_DSN: Optional[str] = Field(None, env="DB_DSN")
    HOST_TCP: str = Field('127.0.0.1', env='HOST_TCP')
    PORT_TCP: int = Field(50000, env='PORT_TCP')

    @validator('DB_DSN', pre=True)
    def assemble_db_dsn(cls, value: Optional[str],
                        values: Dict[str, Any]) -> Any:
        if value:
            return value
        return PostgresDsn.build(
            scheme='postgresql+asyncpg',
            user=values.get("DB_USER"),
            password=values.get("DB_PASS"),
            host=values.get("DB_HOST"),
            port=values.get("DB_PORT"),
            path=f"/{values.get('DB_NAME') or ''}",
        )

    class Config:
        env_file = '../../.env'
        env_nested_delimiter = '__'


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = Settings()