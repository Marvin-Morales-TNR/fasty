from app.models.user_table import Users
from app.models.sqlmodel_config import engine
from app.utils.defaults import create_sha256_hash
from sqlmodel import Session, select

## Schemas
from app.schemas.user_table_schema import RegisterRequest


class RegisterController(object):
    def __init__(self, nonce: int) -> None:
        self.nonce = nonce

    @classmethod
    def check_if_user_exists(self, user_data: RegisterRequest) -> bool:
        try:
            with Session(engine) as session:
                statement = select(Users).where(Users.email == user_data.email)
                results = session.exec(statement).first()
                if not results:
                    return True
                else:
                    return False
        except OSError as error:
            return False

    @classmethod
    def create_new_user(self, user_data: RegisterRequest) -> bool:
        try:
            new_user = Users(
                email=user_data.email,
                first_name=user_data.first_name,
                last_name=user_data.last_name,
                device=user_data.device,
                phone_number=user_data.phone_number,
                address=user_data.address,
                ip_address=user_data.ip_address,
                last_date=user_data.last_date,
                password=create_sha256_hash(user_data.password),
            )
            session = Session(engine)
            session.add(new_user)
            session.commit()
            return True
        except OSError as error:
            return False
