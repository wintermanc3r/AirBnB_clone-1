#!/usr/bin/python3
from models.base_model import Base
from models import *
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    if 'HBNB_TYPE_STORAGE' in os.environ \
       and os.environ['HBNB_TYPE_STORAGE'] == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
