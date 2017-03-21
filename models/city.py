#!/usr/bin/python3
from models import *
import os
from models.base_model import Base
from models.state import State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(BaseModel, Base):
    if os.environ['HBNB_TYPE_STORAGE'] == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey(State.id), nullable=False)
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
