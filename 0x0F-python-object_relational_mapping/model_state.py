#!/usr/bin/python3
"""
definition of state
"""
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Representation of a state"""
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
    #states = relationship("States", back_populates="state")
