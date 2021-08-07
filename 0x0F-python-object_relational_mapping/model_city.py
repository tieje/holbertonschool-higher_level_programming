#!/usr/bin/python3
"""
definition of city
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Representation of a city"""
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(states.id, nullable=False)
