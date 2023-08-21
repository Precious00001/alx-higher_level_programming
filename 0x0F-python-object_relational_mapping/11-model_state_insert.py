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
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(
                                        sys.argv[1],
                                        sys.argv[2],
                                        sys.argv[3]
                                            ),
                            pool_pre_ping=True
                                )
    session = Session(engine)
    State_new = State(name="Louisiana")
    re = session.add(State_new)
    session.commit()
    print(State_new.id)
    session.close()
