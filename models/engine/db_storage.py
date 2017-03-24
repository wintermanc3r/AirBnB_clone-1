#!/usr/bin/python3
import sys
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        uname = os.environ['HBNB_MYSQL_USER']
        upass = os.environ['HBNB_MYSQL_PWD']
        dbname = os.environ['HBNB_MYSQL_DB']
        host = os.environ['HBNB_MYSQL_HOST']
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(uname, upass, host, dbname))
        if 'HBNB_MYSQL_ENV' in os.environ and \
           os.environ['HBNB_MYSQL_ENV'] == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        retval = {}
        if cls is not None:
            for instance in self.__session.query(cls):
                retval.update(instance.id, instance)
            return (retval)
        else:
            for cls in ["User", "State", "City", "Amenity", "Place", "Review"]:
                cls = getattr(sys.modules["models"], cls)
                for instance in self.__session.query(cls):
                    retval.update({instance.id: instance})
            return(retval)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        Base.metadata.create_all(self.__engine)
