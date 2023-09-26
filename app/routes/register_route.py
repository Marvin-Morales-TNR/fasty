from datetime import datetime
from app.utils.logging import Loggin
from fastapi import APIRouter, Request, Response
from app.utils.defaults import config_file_caller
from app.decorators.defaults import endpoint_data_logger
from app.controllers.register_controller import RegisterController

# Schemas
from app.schemas.main import BaseResponse
from app.schemas.user_table_schema import RegisterRequest
from app.schemas.main_controller_schema import RetrievedObject

config = config_file_caller()

register = APIRouter(
    prefix=config["context_prefix"],
    tags=config["routes"]["register_route"]["tags"],
    responses={404: {"description": "Not found"}},
)

logger = Loggin()
controller = RegisterController(12.8)


@register.post("/register", response_model=BaseResponse)
@endpoint_data_logger
async def register_route(
    request: Request, response: Response, body: RegisterRequest
) -> BaseResponse:
    try:
        body.device_type = request.headers["user-agent"]
        body.ip_address = request.client[0]
        body.last_date = datetime.now().strftime("%Y-%m-%d")
        if controller.check_if_user_exists(body):
            controller.create_new_user(body)
        else:
            return BaseResponse(
                data=None, success=False, error=config["error_catalog"]["0"]
            )
        return BaseResponse(success=True, error=False, data="")
    except OSError as error:
        return BaseResponse(success=False, error=True, data=str(error))
