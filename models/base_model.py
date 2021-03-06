#!/usr/bin/python3
import os
from datetime import datetime
import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime


if ("HBNB_TYPE_STORAGE" in os.environ and
   os.environ["HBNB_TYPE_STORAGE"] == "db"):
    Base = declarative_base()
else:
    Base = object


class BaseModel():
    """The base class for all storage objects in this project"""
    if "HBNB_TYPE_STORAGE" in os.environ \
       and os.environ["HBNB_TYPE_STORAGE"] == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(
            DateTime, nullable=False, default=datetime.now())
        updated_at = Column(
            DateTime, default=datetime.now(),
            onupdate=datetime.now(),
            nullable=False)

    def __init__(self, *args, **kwargs):
        """initialize class object"""
        self.created_at = datetime.now()
        self.id = str(uuid.uuid4())
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def save(self):
        """method to update self"""
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

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

    def delete(self):
        from models import storage
        storage.delete(self)
