#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    calistate = State(name='California')
    snfrcity = City(name='San Francisco')
    calistate.cities.append(snfrcity)

    session.add(calistate)
    session.commit()
    session.close()
