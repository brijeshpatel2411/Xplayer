import os

from dotenv import load_dotenv
from pydantic import PostgresDsn

load_dotenv(os.getenv("ENV_FILE", ".env"))

class Config:
    PROJECT_NAME: str = "DADDY VIDEO FASTAPI PROJECT"
    PROJECT_DESCRIPTION: str = f"{PROJECT_NAME} API document."

    POSTGRES_USER: str = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD: str = os.environ["POSTGRES_PASSWORD"]
    POSTGRES_PORT: str = os.environ["POSTGRES_PORT"]
    POSTGRES_SERVER: str = os.environ["POSTGRES_SERVER"]
    POSTGRES_DB: str = os.environ["POSTGRES_DB"]

    @staticmethod
    def assemble_db_connection():
        return PostgresDsn.build(
            scheme="postgresql",
            username=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            port=int(os.environ["POSTGRES_PORT"]),
            host=os.environ["POSTGRES_SERVER"],
            path=os.environ["POSTGRES_DB"] or "",
        ).unicode_string()

