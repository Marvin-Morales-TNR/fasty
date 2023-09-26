from app.schemas.login_schemas import LoginCredentials

class ChangePasswordCredentials(LoginCredentials):
   repeat_password: str