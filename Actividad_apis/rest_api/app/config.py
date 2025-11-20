# config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    REST_PORT: int = 8000

    class Config:
        env_file = "../.env"   # docker-compose usa env_file, local puedes crear .env en root

settings = Settings()
