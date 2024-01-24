from typing import Optional
from pydantic import BaseModel, Field

class Price(BaseModel):   
    id: Optional[str] = Field(default=None)
    typeVehicle: str
    description: Optional[str] = Field(default=None)
    price: int
