#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()

    n_state = State(name='Louisiana')
    session.add(n_state)
    session.commit()
    print('{0}'.format(n_state.id))
    session.close()
