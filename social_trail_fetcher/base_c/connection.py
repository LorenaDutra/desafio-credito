import os

from pymodm import connect


LOCALHOST_URL = 'mongodb://mongo:27017/bureau'
MONGO_URL = os.getenv('MONGO_URL', LOCALHOST_URL)


def get_connection():
    connect(MONGO_URL)
