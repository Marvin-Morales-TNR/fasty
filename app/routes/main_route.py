from fastapi import APIRouter, Request, Response
from app.utils.logging import Loggin
from app.controllers.main_controller import Main_Controller

## Schemas
from app.schemas.object_db import ObjectDB, EmailBody
from app.schemas.main import BaseResponse
from app.schemas.main_controller_schema import RetrievedObject

auth = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

logger = Loggin()
controller = Main_Controller(12.8)


@auth.get("/{info}/retrieve", response_model=BaseResponse)
async def root_route(info: str, request: Request) -> BaseResponse:
    try:
        route = request.url.path
        method = request.method
        code = Response().status_code
        resp = controller.retrieve_data_from_DB(info)
        return BaseResponse(success=True, error=False, data=resp)
    except OSError as err:
        logger.log_request(route, method, code, str(err))
        return BaseResponse(success=False, error=True, data=err)



@auth.post("/insert/{name}", response_model=BaseResponse)
async def root_route(email: EmailBody, name: str, request: Request) -> BaseResponse:
    try:
        result = ObjectDB(user_name=name, email=email.email)
        controller.save_data_in_DB(result)
        return BaseResponse(success=True, error=False, data="")
    except OSError as err:
        logger.log_request(route, method, code, str(err))
