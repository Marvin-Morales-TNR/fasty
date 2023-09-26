from sqlmodel import Field, SQLModel
from typing import Optional

class Users(SQLModel, table=True):
   id: Optional[int] = Field(default=None, primary_key=True)
   first_name: str = Field(max_length=50, nullable=False, default=None)
   last_name: str = Field(max_length=50, nullable=False, default=None)
   email: str = Field(max_length=50, nullable=False, default=None)
   password: str = Field(max_length=64, nullable=False, default=None)
   ip_address: str = Field(max_length=100, nullable=False, default=None)
   last_date: str = Field(max_length=30, nullable=False, default=None)
   device: str = Field(max_length=300, nullable=True, default=None)
   phone_number: str = Field(max_length=16, nullable=False, default=None)
   address: str = Field(max_length=60, nullable=False, default=None)