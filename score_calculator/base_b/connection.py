import os

from sqlalchemy import create_engine


LOCALHOST_URL = 'mysql://bureau:bureau@localhost/bureau'
MYSQL_URL = os.getenv('MYSQL_URL', LOCALHOST_URL)


def get_engine():
    return create_engine(MYSQL_URL)

