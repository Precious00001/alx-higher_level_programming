#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_n = State(name='Louisiana')
    session.add(state_n)
    instance_new = session.query(State).filter_by(name='Louisiana').first()
    print(instance_new.id)
    session.commit()
