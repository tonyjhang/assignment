from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from app.models.Task import create
from app.config.db import config

engine = create_engine(config)

if database_exists(engine.url) is not True:
    create_database(engine.url)

create(engine)