from typing import Optional
from pydantic import BaseModel, Field


class Parkingslot(BaseModel):   
    id: Optional[str] = Field(default=None)
    number: int
    busyStatus: bool