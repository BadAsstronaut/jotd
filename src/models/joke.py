'''
Models for the joke of the day

Note that for more complex models, additional input validation and handling
would be extended here.

We're following the repository pattern, so this exists somewhat by-convention
'''

from typing import Tuple

from repository import joke as joke_repo
from utils.types import JOTD, JOTDInput


def create_jotd(jotd: JOTDInput) -> Tuple[JOTD | None, int]:
    ''' Creates a new JOTD '''
    return joke_repo.create_jotd(
        jotd.text, jotd.date, jotd.description)


def get_jotd_by_id(jotd_id: int) -> Tuple[JOTD | None, int]:
    ''' Gets a JOTD by id '''
    return joke_repo.get_jotd_by_id(jotd_id)


def get_jotd_by_date(date: str) -> Tuple[JOTD | None, int]:
    ''' Gets a JOTD by date '''
    return joke_repo.get_jotd_by_date(date)


def update_jotd(jotd_id: int, jotd: JOTDInput) -> Tuple[JOTD | None, int]:
    ''' Updates a JOTD by id '''
    return joke_repo.update_jotd(jotd_id, jotd.text, jotd.date, jotd.description)


def delete_jotd(jotd_id: int) -> Tuple[None, int]:
    ''' Deletes a JOTD by id; returns None and an error code to conform to the API '''
    return joke_repo.delete_jotd(jotd_id)
