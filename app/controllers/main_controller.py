from typing import List
from app.models.sqlmodel_config import engine
from app.models.user_table import User
from sqlmodel import Field, Session, SQLModel, create_engine, select

## Schemas
from app.schemas.object_db import ObjectDB
class Main_Controller(object):
   def __init__(self, nonce: int) -> None:
      self.nonce = nonce

   def calculate_block(self, block_len: int) -> int | float:
      return (self.nonce * 0.2) + block_len

   def retrieve_post(self, information: str) -> str:
      return information + str(self.nonce)

   def save_data_in_DB(self, data: ObjectDB) -> bool | OSError:
      try:
         session = Session(engine)
         session.add(User(username=data.user_name, email=data.email))
         session.commit()
         return True
      except OSError as err:
         return err

   def retrieve_data_from_DB(self, data: str) -> List[User] | OSError:
      try:
         with Session(engine) as session:
            statement = select(User).where(User.username == data)
            results = session.exec(statement)
            response = [val.dict() for val in results]
         return response
      except OSError as err:
         return err
