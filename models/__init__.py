#!/usr/bin/python3

from os import getenv

"""import the file_storage engine and db storage class from the models engine directory"""

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload() 



