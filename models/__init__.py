#!/usr/bin/python3
"""
Initialization of models package
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
