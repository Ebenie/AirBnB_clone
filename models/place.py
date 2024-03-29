#!/usr/bin/python3
""" This module to define Place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class """
    city_id = ""
    user_id = ""
    name = ""
    amenity_ids = []
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0

