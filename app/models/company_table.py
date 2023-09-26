from sqlmodel import Field, SQLModel
from typing import Optional

class Companies(SQLModel, table=True):
   id: Optional[int] = Field(default=None, primary_key=True)
   company_name: str = Field(max_length=50, nullable=False, default=None)
   company_ruc: str = Field(max_length=50, nullable=False, default=None)