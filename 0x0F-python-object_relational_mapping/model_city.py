#!/usr/bin/python3
"""sqlalchemy cities module"""


from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from model_state import Base, State


class City(Base):
    """creates city object"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
