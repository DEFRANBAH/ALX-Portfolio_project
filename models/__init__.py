#!/usr/bin/python3

from os import getenv

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
"""import the file_storage engine and db storage class from the models engine directory"""
if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload() 


"""___init__ magic method for models directory"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
 """ in storage object and reload the data from the file storage instanciates the file storage from the file storage class if the db is set to db_ storage and else the  file storage si ds ewr set to none """


