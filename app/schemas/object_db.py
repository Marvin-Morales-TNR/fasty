from pydantic import BaseModel

class ObjectDB(BaseModel):
   user_name: str
   email: str

class EmailBody(BaseModel):
   email: str
