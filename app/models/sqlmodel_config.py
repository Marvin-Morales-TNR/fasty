from os import getenv
from app.models.user_table import Users
from sqlmodel import SQLModel, create_engine

user = getenv("DB_USER")
password = getenv("DB_PASS")
host = getenv("DB_HOST")
db_name = getenv("DB_NAME")

## Data bases URLs
## DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}/{db_name}"
DATABASE_URL = getenv("DB_EXTERNALPOSTGRESQL")

## Conection and tables creation
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)
