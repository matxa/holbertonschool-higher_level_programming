#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = Session(engine)

    state_info = session.query(State, City).\
        filter(City.state_id == State.id).order_by(City.id).all()

    for row in state_info:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))

    session.close()

    Base.metadata.create_all(engine)
