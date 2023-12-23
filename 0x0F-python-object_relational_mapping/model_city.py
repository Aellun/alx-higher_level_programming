#!/usr/bin/python3
"""
this module contains class city with its attributes
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Class that defines each city
    attributes:
        id:uato-generated, unique and not null
        name:str 128 chars and not null
        state_id: ForeignKey and not null
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
