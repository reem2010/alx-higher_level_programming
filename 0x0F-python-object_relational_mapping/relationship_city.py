#!/usr/bin/python3
"""Cities in state"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """city class"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
