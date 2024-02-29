from fastapi import APIRouter

from src.video.api import video_router

api_router = APIRouter()

api_router.include_router(video_router, include_in_schema=True, tags=["Video"])