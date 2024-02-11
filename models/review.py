#!/usr/bin/python3
""" This odule for Review class """
from models.base_model import BaseModel

class Review(BaseModel):
    """ Review class also set empty string for attributes"""
    place_id = ""
    user_id = ""
    text = ""
