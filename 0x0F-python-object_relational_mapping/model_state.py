#!/usr/bin/python3
"""
Write a python file that contains the class
definition of a State
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

    """
    Class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
