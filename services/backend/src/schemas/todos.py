from datetime import datetime

from pydantic import BaseModel
from src.schemas.users import UserOut


class TodoBase(BaseModel):
    task: str
    detail: str | None = None


class TodoOut(TodoBase):
    id: int
    due_date: datetime
    finished: bool
    owner: UserOut

    class Config:
        orm_mode = True


class TodoIn(TodoBase):
    due_date: datetime
    finished: bool = False
