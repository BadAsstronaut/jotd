from fastapi import FastAPI, HTTPException

from models.joke import create_jotd, get_jotd_by_id, get_jotd_by_date, update_jotd, delete_jotd
from utils.types import JOTDInput

app = FastAPI()


@app.post("/jotd/create")
async def create_joke(jotd: JOTDInput):
    new_jotd, code = create_jotd(jotd)
    if code != 201:
        raise HTTPException(status_code=code)
    return {"jotd": new_jotd}


@app.get("/jotd/{jotd_id}")
async def read_joke(jotd_id: int):
    jotd, code = get_jotd_by_id(jotd_id)
    if code != 200:
        raise HTTPException(status_code=code)
    return {"jotd": jotd}


@app.get("/jotd/date/{date}")
async def read_joke_date(date: str):
    jotd, code = get_jotd_by_date(date)
    if code != 200:
        raise HTTPException(status_code=code)
    return {"jotd": jotd}


@app.put("/jotd/{jotd_id}")
async def update_joke(jotd_id: int, jotd: JOTDInput):
    updated_jotd, code = update_jotd(jotd_id, jotd)
    if code != 200:
        raise HTTPException(status_code=code)
    return {"jotd": updated_jotd}


@app.delete("/jotd/{jotd_id}")
async def delete_joke(jotd_id: int):
    _, code = delete_jotd(jotd_id)
    if code != 200:
        raise HTTPException(status_code=code)
    return {"message": "jotd deleted"}
