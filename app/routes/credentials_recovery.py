from fastapi import APIRouter, Request, Response
from app.schemas.main import BaseResponse
from app.utils.defaults import config_file_caller
from app.decorators.defaults import endpoint_data_logger

config = config_file_caller()

credentials = APIRouter(
    prefix=config["context_prefix"],
    tags=config["routes"]["credentials_route"]["tags"],
    responses={404: {"description": "Not found"}},
)


@credentials.get("/credentials", response_model=BaseResponse)
@endpoint_data_logger
async def root_router(request: Request, response: Response) -> BaseResponse:
    try:
        return BaseResponse(success=False, error=True, data="root")
    except OSError as err:
        return BaseResponse(success=False, error=True, data="Server error")
