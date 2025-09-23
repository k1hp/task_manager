from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class PostgresConfig(BaseModel):
    name: str
    user: str
    password: str
    host: str = 'localhost'
    port: int


class RedisConfig(BaseModel):
    name: str


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", env_nested_delimiter="__")
    postgres: PostgresConfig
    redis: RedisConfig

config = Config()

if __name__ == '__main__':
    print(Config().model_dump())