from functools import lru_cache
from pydantic import Field
from pydantic import BaseSettings


class Settings(BaseSettings):
    HOST_TCP: str = Field('127.0.0.1', env='HOST_TCP')
    PORT_TCP: int = Field(50000, env='PORT_TCP')

    class Config:
        env_file = '../.env'
        env_nested_delimiter = '__'


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
