#!/usr/bin/python3
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'State'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    states = relationship("States", back_populates="state")
