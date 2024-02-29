from src.video.schemas import (
    VideoDataBase,
    VideoDataUpdate,
    SliderImgBase,
    SliderImgUpdate,
)
from src.video.models import VideoData, SliderImg
from utils.crud.base import CRUDBase


class VideoCRUD(CRUDBase[VideoData, VideoDataBase, VideoDataUpdate]):
    pass


video_crud = VideoCRUD(VideoData)


class SliderCRUD(CRUDBase[SliderImg, SliderImgBase, SliderImgUpdate]):
    pass

slider_crud = SliderCRUD(SliderImg)