#!/usr/bin/python3
"""
definition of state
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Representation of a state"""
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
