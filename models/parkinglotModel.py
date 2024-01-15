from typing import Annotated, Optional
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

PyObjectId = Annotated[str, BeforeValidator(str)]

class Parkinglot(BaseModel):   
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    number: str | int
    busyStatus: bool
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )
