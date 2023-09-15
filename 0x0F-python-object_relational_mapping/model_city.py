#!/usr/bin/python3
"""Cities in state"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """city class"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('State.id'))
