from pydantic import BaseModel
from typing import TypeVar

T = TypeVar("T")

class BaseResponse(BaseModel):
   success: bool | None
   error: bool | str | None
   data: T
