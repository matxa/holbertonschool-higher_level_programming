#!/usr/bin/python3
"""SQLAlchemy practice"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class States(Base):
    

engine = create_engine('mysql+mysqlconnector://{}', echo=True)

(host="localhost", port=3066, charset="utf8",
                                 user=argv[1], passwd=argv[2], db=argv[3])

