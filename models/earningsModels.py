from typing import Annotated, Optional
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field
import datetime
PyObjectId = Annotated[str, BeforeValidator(str)]

class Earnings(BaseModel):   
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    date: datetime.date = Field(format="YYYY-MM-DD")
    earnings: int
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )