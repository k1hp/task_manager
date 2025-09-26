from pathlib import Path

from pydantic import BaseModel, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent

class PostgresConfig(BaseModel):
    user: str
    password: str
    database: str
    host: str = 'localhost'
    port: int

    @computed_field
    @property
    def sqlalchemy_url(self) -> str:
        return f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"



class RedisConfig(BaseModel):
    name: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_nested_delimiter="__")
    postgres: PostgresConfig
    redis: RedisConfig

settings = Settings()

if __name__ == '__main__':
    print(settings.model_dump())
    print(settings.postgres.sqlalchemy_url)