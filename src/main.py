import logging

from fastapi import FastAPI, HTTPException

from models import joke as joke_models
from utils.types import JOTDInput

app = FastAPI()


logging.basicConfig(level=logging.INFO)


@app.post("/jotd")
async def create_joke(jotd: JOTDInput):
    ''' Creates a new joke of the day '''
    new_jotd, code = joke_models.create_jotd(jotd)
    if code != 201:
        raise HTTPException(status_code=code)
    return {"jotd": new_jotd}


@app.get("/jotd/{jotd_id}")
async def read_joke(jotd_id: int):
    ''' Gets a joke of the day by id '''
    jotd, code = joke_models.get_jotd_by_id(jotd_id)
    if code != 200:
        raise HTTPException(status_code=code)
    return {"jotd": jotd}


@app.get("/jotd/date/{date}")
async def read_joke_date(date: str):
    ''' Gets a joke of the day by date '''
    jotd, code = joke_models.get_jotd_by_date(date)
    if code != 200:
        raise HTTPException(status_code=code)
    return {"jotd": jotd}


@app.put("/jotd/{jotd_id}")
async def update_joke(jotd_id: int, jotd: JOTDInput):
    ''' Updates a joke of the day by id '''
    updated_jotd, code = joke_models.update_jotd(jotd_id, jotd)
    if code != 200:
        raise HTTPException(status_code=code)
    return {"jotd": updated_jotd}


@app.delete("/jotd/{jotd_id}")
async def delete_joke(jotd_id: int):
    ''' Deletes a joke of the day by id '''
    _, code = joke_models.delete_jotd(jotd_id)
    if code != 204:
        raise HTTPException(status_code=code)
    return {"message": "jotd deleted"}
