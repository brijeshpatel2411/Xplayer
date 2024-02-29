from fastapi import FastAPI

from src.api_handler import api_router
from src.config import Config

app = FastAPI()

def create_app():
    app = FastAPI(
        title=Config.PROJECT_NAME,
        description=Config.PROJECT_DESCRIPTION
    )

    app.include_router(api_router)

    @app.get("/", tags=["API Base"])
    def _get():
        return f"Welcome to {Config.PROJECT_NAME} APIs. Up and running!"

    return app
