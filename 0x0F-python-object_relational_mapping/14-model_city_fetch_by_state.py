#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    conn = "mysql+mysqldb"
    engine = create_engine('{}://{}:{}@localhost/{}'.format(
        conn, argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State, City).filter(City.state_id == State.id).all()

    for state, city in data:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
