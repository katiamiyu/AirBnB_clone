#!/usr/bin/python3
""" initialize storage here """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
