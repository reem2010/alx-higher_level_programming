#!/usr/bin/python3
"""First state model"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship 
Base = declarative_base()


class State(Base):
    """state class"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
