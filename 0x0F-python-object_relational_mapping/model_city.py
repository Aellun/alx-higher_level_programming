#!/usr/bin/python3
"""
Contains the class definition of a City:
city class:
            inherits from base
            links table cities
            id is auto generated and not null
            name is 128 char and not null
            state_id ForeignKey and not null
module: sqlAlchemy
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
