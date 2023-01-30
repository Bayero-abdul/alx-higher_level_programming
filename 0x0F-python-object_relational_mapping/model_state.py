#!/usr/bin/env python3
"""contains the class definition of a State and \
an instance Base = declarative_base()

"""


from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Mapped to table `states`."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128))
