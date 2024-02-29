from uuid import uuid4
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import as_declarative
from sqlalchemy.ext.declarative import declarative_base
from utils.session import Base
from utils.db.base import ModelBase, ModelBaseField

str_uuid = lambda: str(uuid4())

# @as_declarative()
class SliderImg(ModelBase):
    __tablename__ = 'slider_img'

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    img_link = Column(String, nullable=True)


class VideoData(ModelBase, ModelBaseField):
    __tablename__ = 'videodata'

    title = Column(Text, nullable=True)
    url = Column(Text, nullable=False)
    upload_time = Column(Text, nullable=False)
    video_time = Column(Text, nullable=False)
    porn_star = Column(Text, nullable=False)
    category = Column(Text, nullable=False)
    video_url = Column(Text, nullable=False)
    main_thumb = Column(Text, nullable=False)
    image_thumb = Column(Text, nullable=False)
