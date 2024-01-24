from typing import Optional
from pydantic import BaseModel, Field
import datetime

class Historical(BaseModel):
    id: Optional[str] = Field(default="")
    plate: str
    # date: Optional[datetime.datetime] = Field(default_factory=datetime.datetime.today().date, format="YYYY-MM-DD")  # Eliminado
    checkInTime: datetime.datetime = Field(default_factory=datetime.datetime.now, format="%Y-%m-%dT%H:%M:%S")  # Combina fecha y hora
    checkOutTime: Optional[datetime.datetime] = Field(format="%Y-%m-%dT%H:%M:%S", default=None)
    totalValue: Optional[int] = Field(default=0)
    itsPaid: Optional[bool] = Field(default=False)
