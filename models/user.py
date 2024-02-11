#!/usr/bin/python3
""" This module for User class 
to be used in the console.py"""
from models.base_model import BaseModel

class User(BaseModel):
    """ User class set empty string 
    for all attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
