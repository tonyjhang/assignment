from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    status = Column(Integer)

def create(engine):
    Base.metadata.create_all(engine)