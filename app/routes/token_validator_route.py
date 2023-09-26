from fastapi import APIRouter, Request, Response
from app.utils.defaults import config_file_caller
from app.decorators.defaults import token_verification_required, endpoint_data_logger

# Schemas
from app.schemas.main import BaseResponse

config = config_file_caller()

token_validator = APIRouter(
    prefix=config["context_prefix"],
    tags=config["routes"]["token_validator"]["tags"],
    responses={404: {"description": "Not found"}},
)


@token_validator.get("/token-validation", response_model=BaseResponse)
@endpoint_data_logger
@token_verification_required
async def token_validation(request: Request) -> BaseResponse:
    response = {"validated": True}
    return BaseResponse(success=True, error=False, data=response)
