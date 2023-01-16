'''
Joke repository.

This module contains functions that interact with the database.
'''

from functools import wraps
from typing import Tuple
import logging

from repository.db import Session, JOTD
from utils import globals, types


def internal_err_handler(func):
    '''
    Decorator that handles uncaught errors and returns None and an error code.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            logging.exception(ex)
            return None, globals.HTTP_INTERNAL_SERVER_ERROR
    return wrapper


@internal_err_handler
def create_jotd(text: str, date: str, description: str | None) -> Tuple[types.JOTD | None, int]:
    ''' Creates a new JOTD '''
    logging.info(f'Creating JOTD: {text} ({date})')
    with Session() as session:
        jotd = JOTD(text=text, date=date, description=description)
        session.add(jotd)
        session.commit()
        session.refresh(jotd)
        assert jotd.id is not None
        assert jotd.text is not None
        assert jotd.date is not None

    return (types.JOTD(id=jotd.id,
                       text=jotd.text,
                       date=jotd.date,
                       description=jotd.description),
            globals.HTTP_CREATED)


@ internal_err_handler
def get_jotd_by_id(jotd_id: int) -> Tuple[types.JOTD | None, int]:
    ''' Gets a JOTD by id '''
    with Session() as session:
        jotd = session.query(JOTD).filter(JOTD.id == jotd_id).first()
        if jotd is None:
            return None, globals.HTTP_NOT_FOUND
    return jotd, globals.HTTP_OK


@ internal_err_handler
def get_jotd_by_date(date: str) -> Tuple[types.JOTD | None, int]:
    ''' Gets a JOTD by date '''
    logging.info(f'Reading JOTD by date: {date}')
    with Session() as session:
        jotd = session.query(JOTD).filter(JOTD.date == date).first()
        if jotd is None:
            return None, globals.HTTP_NOT_FOUND
    return jotd, globals.HTTP_OK


@ internal_err_handler
def update_jotd(jotd_id: int, text: str, date: str, description: str | None) -> Tuple[types.JOTD | None, int]:
    ''' Updates a JOTD by id '''
    logging.info(f'Updating JOTD: {text} ({date}')
    with Session() as session:
        jotd = session.query(JOTD).filter(JOTD.id == jotd_id).first()
        if jotd is None:
            return None, globals.HTTP_NOT_FOUND
        jotd.text = text
        jotd.date = date
        jotd.description = description
        session.commit()
        session.refresh(jotd)

    return (types.JOTD(id=jotd.id,
                       text=jotd.text,
                       date=jotd.date,
                       description=jotd.description),
            globals.HTTP_OK)


@ internal_err_handler
def delete_jotd(jotd_id: int) -> Tuple[None, int]:
    ''' Deletes a JOTD by id; returns None and an error code to conform to the API '''
    logging.info(f'Deleting JOTD: {jotd_id}')
    with Session() as session:
        jotd = session.query(JOTD).filter(JOTD.id == jotd_id).first()
        if jotd is None:
            return None, globals.HTTP_NOT_FOUND
        session.delete(jotd)
        session.commit()
    return None, globals.HTTP_NO_CONTENT
