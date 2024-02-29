from typing import List, Optional
from pydantic import BaseModel


class SliderImgUpdate(BaseModel):
    img_link: Optional[List[str]] = None


class SliderImgBase(SliderImgUpdate):
    pass


class VideoDataUpdate(BaseModel):
    title: Optional[str] = None
    url: Optional[str] = None
    upload_time: Optional[str] = None
    video_time: Optional[str] = None
    porn_star: Optional[str] = None
    category: Optional[str] = None
    video_url: Optional[str] = None
    main_thumb: Optional[str] = None
    image_thumb: Optional[str] = None

class VideoDataBase(VideoDataUpdate):
    id: Optional[str] = None


class VideoDataRequest(VideoDataUpdate):
    pass

class ScrapeRequest(BaseModel):
    url: str

class VideoLinkResponse(BaseModel):
    link_360: str
    link_720: str
    link_1080: str
    poster: str


class VideoDataBaseResponse(BaseModel):
    video_data: VideoDataBase
    link_data: VideoLinkResponse
