#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy import update
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm.exc import NoResultFound


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = Session(engine)

    id_2 = session.query(State).get(2)
    id_2.name = "New Mexico"

    session.commit()
    session.close()

    Base.metadata.create_all(engine)
