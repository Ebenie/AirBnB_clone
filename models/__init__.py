#!/usr/bin/python3
"""This module initializes the models package
to use in other file like base_mode.py"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

