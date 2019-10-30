import os

from sqlalchemy import create_engine


LOCALHOST_URL = 'postgresql+psycopg2://bureau:bureau@localhost/bureau'
POSTGRES_URL = os.getenv('POSTGRES_URL', LOCALHOST_URL)


def get_engine():
    return create_engine(POSTGRES_URL)

