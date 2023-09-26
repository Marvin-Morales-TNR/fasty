import os
from fastapi import APIRouter, Request, Response
from app.utils.defaults import config_file_caller
from app.decorators.defaults import token_verification_required, endpoint_data_logger
from app.controllers.login_controller import LoginController

# Schemas
from app.schemas.main import BaseResponse
from app.schemas.login_schemas import LoginCredentials

config = config_file_caller()

login = APIRouter(
    prefix=config["context_prefix"],
    tags=config["routes"]["login_route"]["tags"],
    responses={404: {"description": "Not found"}},
)

secret = os.getenv("JWT_SECRET")
login_controller = LoginController(secret)


@login.post("/login", response_model=BaseResponse)
@endpoint_data_logger
async def login_route(
    request: Request, response: Response, body: LoginCredentials
) -> BaseResponse:
    try:
        if login_controller.check_if_user_exists(body.user_name):
            if token := login_controller.validate_credentials_login(body):
                response.headers["Authorization"] = token
                return BaseResponse(success=True, error=False, data="Token generated!")
            else:
                return BaseResponse(
                    success=False, error=config["error_catalog"]["1"], data=None
                )
        else:
            return BaseResponse(
                success=False, error=config["error_catalog"]["2"], data=None
            )
    except OSError as error:
        return BaseResponse(success=False, error=True, data=str(error))


@login.get("/get-users", response_model=BaseResponse)
@endpoint_data_logger
@token_verification_required
async def request_full_user(request: Request, response: Response) -> BaseResponse:
    res = login_controller.request_users_list()
    return BaseResponse(success=True, error=False, data=res)
