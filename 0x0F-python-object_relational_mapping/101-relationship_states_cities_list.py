#!/usr/bin/python3
"""lists all State objects, and corresponding City objects"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    conn = "mysql+mysqldb"
    engine = create_engine('{}://{}:{}@localhost/{}'.format(
        conn, argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).order_by(State.id).all()

    for i in data:
        print(f"{i.id}: {i.name}")
        city = sorted(i.cities, key=lambda city: city.id)
        for j in city:
            print(f"\t{j.id}: {j.name}")

    session.close()
