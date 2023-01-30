#!/usr/bin/python3
"""deletes all State objects with a name containing \
the letter a from the database hbtn_0e_6_usa.

"""


if __name__ == "__main__":
    
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id).all()
    for state, city in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
