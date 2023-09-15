from fastapi import APIRouter
from app.schemas.main import BaseResponse
from app.schemas.main_controller_schema import RetrievedObject
from app.controllers.main_controller import Main_Controller

auth = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

controller = Main_Controller(12.8)

@auth.get("/{info}", response_model=BaseResponse)
async def root_route(info: int) -> BaseResponse:
    result = controller.calculate_block(info)
    response = RetrievedObject(name=result, age=12)
    return BaseResponse(success=True, error=False, data=response)
 
@auth.post("/{info}/authentication", response_model=BaseResponse)
async def root_route(info: int) -> BaseResponse:
    return BaseResponse(success=True, error=False, data=info)