from pydantic import BaseModel


class JOTD(BaseModel):
    id: int
    text: str
    date: str
    description: str | None = None


class JOTDInput(BaseModel):
    text: str
    date: str
    description: str | None = None
