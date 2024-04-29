from datetime import datetime
from uuid import UUID
from uuid import UUID

from pydantic import ConfigDict, BaseModel


#from typing import Optional


class Person(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    per_id: UUID
    ord_id: UUID
    type: str
    info: str



class CreatePersonRequest(BaseModel):
    ord_id: UUID
    type: str
    info: str
