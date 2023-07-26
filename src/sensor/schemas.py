import datetime as datetime
from pydantic import BaseModel


class ControllerSchema(BaseModel):
    created_at: datetime.datetime
    payload: int
