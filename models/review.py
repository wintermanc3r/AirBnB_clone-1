#!/usr/bin/python3
from models import *
import os
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models import Place, User

class Review(BaseModel, Base):
    if os.environ['HBNB_TYPE_STORAGE'] == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey(Place.id), nullable=False)
        user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
