from typing import List
from fastapi import APIRouter, File, UploadFile, status

from utils.session import get_db
from src.video.crud import video_crud, slider_crud
from src.video.scrapping import get_video_urls
from src.video.schemas import (
    VideoDataUpdate,
    VideoDataBase,
    ScrapeRequest,
    VideoDataBaseResponse
)
import pandas as pd

video_router = APIRouter()


@video_router.post(
    "/video", status_code=status.HTTP_201_CREATED, response_model=VideoDataBaseResponse
)
def add_videos(video_req: VideoDataUpdate, db: get_db):
    video = video_crud.create(db, obj_in=VideoDataBase(**video_req.model_dump()))
    video_urls = get_video_urls(video.video_link)
    response = {
        "video_data":video, "link_data":video_urls
    }
    return response


@video_router.get(
    "/video/{id}", status_code=status.HTTP_200_OK, response_model=VideoDataBaseResponse
)
def get_videos(db: get_db, id: str):
    video = video_crud.get(db, id=id)
    video_urls = get_video_urls(video.video_link)
    response = {
        "video_data":video, "link_data":video_urls
    }
    return response


@video_router.get(
    "/videos", status_code=status.HTTP_200_OK, response_model=List[VideoDataBase]
)
def get_all_videos(db: get_db, page: int = 1, per_page: int = 10):
    video = video_crud.get_multi(db, page=page, per_page=per_page)
    return video


@video_router.post("/video/scrape", status_code=status.HTTP_200_OK)
def get_video(scrape_req: ScrapeRequest):
    video_urls = get_video_urls(scrape_req.url)
    return video_urls

@video_router.post("/upload/csv", status_code=status.HTTP_200_OK)
def upload_csv(file: UploadFile, db: get_db):
    csv_file = pd.read_csv(file.file)
    # breakpoint()
    for _, value in csv_file.iterrows():
        value.to_dict()
        data = {
            "title": value["porn_title"],
            "url": value["porn_url"],
            "upload_time": value["upload_time"],
            "video_time": value["video_time"],
            "porn_star": value["porn_star"],
            "category": value["category"],
            "video_url": value["video_url"],
            "main_thumb": value["main_thumb"],
            "image_thumb": value["image_thumb"],
        }
        video_crud.create(db, obj_in=data)