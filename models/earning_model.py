import datetime
from pydantic import BaseModel, Field
from typing import Optional


class Earning(BaseModel):
    id: Optional[str] = Field(default=None)
    date: Optional[str] = Field(default_factory= lambda: datetime.datetime.now().strftime("%Y-%m-%d"),format="YYYY-MM-DD")
    earnings: Optional[int] = Field(default=0)


def get_current_date() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d")