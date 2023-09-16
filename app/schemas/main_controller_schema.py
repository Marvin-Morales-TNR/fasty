from pydantic import BaseModel
from typing import TypeVar, Optional
from .main import BaseResponse

class RetrievedObject(BaseModel):
   name: str
   age: int
   address: Optional[str]
