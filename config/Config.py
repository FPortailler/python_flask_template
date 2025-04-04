import os
from enum import Enum


class Env(Enum):
    DEV = "dev"
    QA = "qa"
    PROD = "prod"
    TEST = "test"


class Config:
    """ Project configuration """
    ENV: Env
    HOST: str
    PORT: str

    # Add any project configuration here

    def __init__(
            self,
            env: Env = Env(os.getenv("ENV", "dev")),
            host: str = os.getenv("HOST", "0.0.0.0"),
            port: str = os.getenv("PORT", "5001"),
    ):
        self.ENV = env
        self.HOST = host
        self.PORT = port


config = Config()
