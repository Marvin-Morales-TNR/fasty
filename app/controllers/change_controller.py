from sqlmodel import Session, select
from app.models.user_table import Users
from app.models.sqlmodel_config import engine
from app.utils.defaults import create_sha256_hash
from app.schemas.login_schemas import ChangePasswordCredentials


class ChangePasswordController(object):
    def check_credentials_and_update_pass(
        self, credentials: ChangePasswordCredentials
    ) -> bool:
        try:
            with Session(engine) as session:
                statement = select(Users).where(Users.email == credentials.user_name)
                result = session.exec(statement).first()
                pass_hashed = create_sha256_hash(credentials.password)
                if result.password == pass_hashed:
                    result.password = create_sha256_hash(credentials.new_password)
                    session.add(result)
                    session.commit()
                    session.refresh(result)
                    return "__SUCCESS__"
                else:
                    raise Exception("Not possible to update the password!")
        except Exception as error:
            return error.args[0]
