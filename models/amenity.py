#!/usr/bin/python3
from models.base_model import Base
from models import *
from sqlalchemy import Column, Integer, String
import os


class Amenity(BaseModel, Base):
    if (os.environ['HBNB_TYPE_STORAGE'] and
        os.environ['HBNB_TYPE_STORAGE'] == "db"):
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
