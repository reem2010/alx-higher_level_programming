#!/usr/bin/python3
""" prints the first State object from the database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    conn = "mysql+mysqldb"
    engine = create_engine('{}://{}:{}@localhost/{}'.format(
        conn, argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).filter(State.id == 1).all()

    for i in data:
        print(f"{i.id}: {i.name}")
    session.close()
