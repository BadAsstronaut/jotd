'''
Creates database, tables, and a sessionmaker.
'''

import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped

database_url = os.getenv('DATABASE_URL', 'sqlite:///jotd.db')

engine = create_engine(database_url)
Base = declarative_base()


class JOTD(Base):
    '''
    Joke of the day DB table

    The ignored type errors are due to requiring a mypy plugin to support mapping sqlalchemy types
    '''
    __tablename__ = 'jotd'
    id: Mapped[int] = Column(Integer,
                             primary_key=True,
                             index=True)  # type: ignore
    text: Mapped[str] = Column(String)  # type: ignore
    date: Mapped[str] = Column(String,
                               index=True)  # type: ignore
    description: Mapped[str | None] = Column(String,
                                             nullable=True)  # type: ignore


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
