'''
Creates database, tables, and a sessionmaker.
'''

import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

database_url = os.getenv('DATABASE_URL', 'sqlite:///jotd.db')

engine = create_engine(database_url)
Base = declarative_base()


class JOTD(Base):
    ''' Joke of the day DB table '''
    __tablename__ = 'jotd'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    date = Column(String, index=True)
    description = Column(String, nullable=True)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
