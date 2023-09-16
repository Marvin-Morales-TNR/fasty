from os import getenv
from sqlmodel import SQLModel
from app.models.user_table import User
from sqlmodel import SQLModel, create_engine

user = getenv('DB_USER')
password = getenv('DB_PASS')
host = getenv('DB_HOST')
db_name = getenv('DB_NAME')

DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}/{db_name}"
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)
