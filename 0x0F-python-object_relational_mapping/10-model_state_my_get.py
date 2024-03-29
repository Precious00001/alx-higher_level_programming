#!/usr/bin/python3
"""
This script prints the State object id
with the name passed as argument
from the database `hbtn_0e_6_usa`.
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    inst = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(inst[0].id)
    except IndexError:
        print("Not found")
