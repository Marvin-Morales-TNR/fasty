from pydantic import BaseModel
from typing import TypeVar

T = TypeVar("T")


class BaseResponse(BaseModel):
    success: bool | None
    error: bool | str | T | None
    data: T
