from fastapi import FastAPI
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from app.utils.defaults import config_file_caller

# Routes
from app.routes.register_route import register
from app.routes.login_route import login
from app.routes.credentials_recovery import credentials
from app.routes.token_validator_route import token_validator
from app.routes.change_password_route import password_changer

app = FastAPI(docs_url="/auth/docs")
load_dotenv()

config = config_file_caller()

app.add_middleware(
    CORSMiddleware,
    allow_origins=config["allow_origins"],
    allow_methods=config["allowed_methods"],
    allow_headers=config["allowed_headers"],
)

app.include_router(register)
app.include_router(login)
app.include_router(credentials)
app.include_router(token_validator)
app.include_router(password_changer)
