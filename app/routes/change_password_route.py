from fastapi import APIRouter, Request
from app.utils.defaults import config_file_caller
from app.schemas.main import BaseResponse
from app.schemas.login_schemas import ChangePasswordCredentials
from app.controllers.change_controller import ChangePasswordController
from app.decorators.defaults import token_verification_required, endpoint_data_logger

config = config_file_caller()

password_changer = APIRouter(
    prefix=config["context_prefix"],
    tags=config["routes"]["change_password"]["tags"],
    responses={404: {"description": "Not found"}},
)

controller = ChangePasswordController()


@password_changer.post("/change-password", response_model=BaseResponse)
@endpoint_data_logger
@token_verification_required
async def change_password(
    request: Request, payload: ChangePasswordCredentials
) -> BaseResponse:
    try:
        result = controller.check_credentials_and_update_pass(payload)
        if result == "__SUCCESS__":
            response = {"status": "Password was changed successfully!"}
            return BaseResponse(success=True, error=False, data=response)
        else:
            raise Exception({"error": result})
    except Exception as err:
        return BaseResponse(
            success=False, error=config["error_catalog"]["6"], data=err.args[0]
        )
