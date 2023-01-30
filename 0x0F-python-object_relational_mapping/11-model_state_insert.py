#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa.

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
    s1 = State(name="Louisiana")
    session.add(s1)
    session.commit()
    print(s1.id)
