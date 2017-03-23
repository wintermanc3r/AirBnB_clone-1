#!/usr/bin/python3
import os
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import *


class State(BaseModel, Base):
    if (os.environ["HBNB_TYPE_STORAGE"] and
        os.environ["HBNB_TYPE_STORAGE"] == "db"):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
