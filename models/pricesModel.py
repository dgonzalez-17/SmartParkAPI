from typing import Annotated, Optional
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

PyObjectId = Annotated[str, BeforeValidator(str)]

class Prices(BaseModel):   
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    typeVehicle: str
    description: str
    price: int
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )

