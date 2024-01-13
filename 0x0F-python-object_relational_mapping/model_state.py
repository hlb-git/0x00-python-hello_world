#!/usr/bin/python3
"""ORM demonstration"""


import sys
from sqlalchemy import create_engine, Column
from sqlalchemy import String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """State class"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name


mysql_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
engine = create_engine(mysql_str.format(sys.argv[1],
                       sys.argv[2], sys.argv[3]), pool_pre_ping=True)

Base.metadata.create_all(bind=engine)
