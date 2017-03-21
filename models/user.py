#!/usr/bin/python3
from models.base_model import Base
from models import *
from sqlalchemy import Column, Integer, String
import os

class User(BaseModel, Base):
    if os.environ['HBNB_TYPE_STORAGE'] == "db":
        __tablename__ = "users"
        name = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
