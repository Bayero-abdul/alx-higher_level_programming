#!/usr/bin/python3
"""prints the State object with the name passed as argument \
from the database hbtn_0e_6_usa.

"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    name = str(argv[4])
    state = session.query(State).filter(State.name == name)\
                   .order_by(State.id).first()

    if state:
        print(state.id)
    else:
        print("Not found")
