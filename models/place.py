#!/usr/bin/python3
from models import *
from models.base_model import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    if (os.environ["HBNB_TYPE_STORAGE"] and
        os.environ["HBNB_TYPE_STORAGE"] == "db"):
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey(City.id), nullable=False)
        user_id = Column(String(60), ForeignKey(User.id), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 viewonly=True)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenities = [""]


class PlaceAmenity(Base):
    if (os.environ["HBNB_TYPE_STORAGE"] and
        os.environ["HBNB_TYPE_STORAGE"] == "db"):
        __tablename__ = "place_amenity"
        place_id = Column(String(60), ForeignKey(Place.id),
                          primary_key=True, nullable=False)
        amenity_id = Column(String(60), ForeignKey(Amenity.id),
                            primary_key=True, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__()
