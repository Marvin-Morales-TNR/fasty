from pydantic import BaseModel

class RegisterRequest(BaseModel):
   email: str
   first_name: str
   last_name: str
   device: str
   phone_number: str
   address: str
   ip_address: str
   last_date: str
   password: str