import jwt
from datetime import datetime, timedelta
from sqlmodel import Session, select
from app.models.user_table import Users
from app.models.sqlmodel_config import engine
from app.utils.defaults import config_file_caller
from app.utils.defaults import create_sha256_hash

## Schemas
from app.schemas.login_schemas import PayloadCredentials, LoginCredentials

config = config_file_caller()


class LoginController(object):
    def __init__(self, jwt_key: str) -> None:
        self.jwt_key = jwt_key

    def token_generator(self, payload: PayloadCredentials) -> str:
        final_payload = {**payload, "exp": datetime.utcnow() + timedelta(days=30)}
        return jwt.encode(final_payload, self.jwt_key, algorithm="HS256")

    def decode_token(self, token: str) -> bool | dict:
        try:
            payload = jwt.decode(token, self.jwt_key, algorithms=["HS256"])
            return True
        except jwt.ExpiredSignatureError:
            return config["error_catalog"]["3"]
        except jwt.DecodeError:
            return config["error_catalog"]["4"]
        except jwt.InvalidTokenError:
            return config["error_catalog"]["5"]

    def check_if_user_exists(self, email: str) -> bool:
        try:
            with Session(engine) as session:
                statement = select(Users.email).where(Users.email == email)
                return session.exec(statement).first() is not None
        except OSError as error:
            return str(error)

    def validate_credentials_login(
        self, credentials: LoginCredentials
    ) -> str | bool | dict:
        try:
            with Session(engine) as session:
                statement = select(Users.password).where(
                    Users.email == credentials.user_name
                )
                result = session.exec(statement).first()
                if result == create_sha256_hash(credentials.password):
                    payload = PayloadCredentials(
                        user_name=credentials.user_name, role="user"
                    )
                    return self.token_generator({**payload.dict()})
                else:
                    return False
        except OSError as error:
            return str(error)

    def request_users_list(self) -> list[str] | str:
        try:
            with Session(engine) as session:
                result = session.exec(select(Users.email))
                return [item for item in result]
        except OSError as error:
            return str(error)
