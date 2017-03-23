#!/usr/bin/python3
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review

if "HBNB_TYPE_STORAGE" in os.environ \
   and os.environ["HBNB_TYPE_STORAGE"] == "db":
    from models.engine import db_storage
    storage_type = "db"
    storage = db_storage.DBStorage()
    storage.reload()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()
    storage.reload()
    storage_type = "file"
