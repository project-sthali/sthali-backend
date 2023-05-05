import configparser
from pydantic import BaseModel, BaseSettings, validator

from fastapi.middleware.cors import CORSMiddleware


class CORSConfig(BaseModel):
    allow_credentials: bool
    allow_headers: list
    allow_methods: list
    allow_origins: list

    @validator('allow_headers', 'allow_methods', 'allow_origins', pre=True)
    def eval_lists(cls, v):
        return eval(v)


class DBConfig(BaseModel):
    database: str
    host: str
    password: str
    port: int
    username: str


class Config(BaseSettings):
    cors: CORSConfig
    db: DBConfig


config = configparser.ConfigParser()
config.read('config.cfg')
config_data = dict(config)
config_data.pop('DEFAULT')

CONFIG = Config(**config_data)


def config_app(app, config: CORSConfig) -> None:
    app.add_middleware(CORSMiddleware, **dict(config))
