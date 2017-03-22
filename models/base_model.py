#!/usr/bin/python3
import datetime
import uuid
from models import *
import models
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime

if storage_type == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel():
    """The base class for all storage objects in this project"""
    if storage_type == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(
            DateTime, nullable=False, default=datetime.datetime.now())
        last_updated = Column(
            DateTime, default=datetime.datetime.now(),
            onupdate=datetime.datetime.now())
        name = Column(String(128), nullable=False)

    def __init__(self, **kwargs):
        """initialize class object"""
        self.created_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        print(kwargs)
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.save()

    def save(self):
        """method to update self"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """edit string representation"""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        """convert to json"""
        dupe = self.__dict__.copy()
        dupe["created_at"] = str(dupe["created_at"])
        if ("updated_at" in dupe):
            dupe["updated_at"] = str(dupe["updated_at"])
        dupe["__class__"] = type(self).__name__
        if "_sa_instance_state" in dupe:
            del(dupe["_sa_instance_state"])
        return dupe
