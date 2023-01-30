#!/usr/bin/env python3
"""contains the class definition of a City.

"""


from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """Mapped to table `cities`."""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
