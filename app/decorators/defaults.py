import os
from typing import Callable
from functools import wraps
from fastapi import Request, Response
from app.schemas.main import BaseResponse
from app.controllers.login_controller import LoginController

secret = os.getenv("JWT_SECRET")


def token_verification_required(decored_function: Callable) -> Callable:
    @wraps(decored_function)
    async def wrapper(request: Request, *args, **kwargs):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        authentication = LoginController(secret)
        decoded = authentication.decode_token(token)
        if isinstance(decoded, bool) and decoded:
            return await decored_function(request, *args, **kwargs)
        else:
            return BaseResponse(success=False, error=decoded, data=None)

    return wrapper


def endpoint_data_logger(decored_function: Callable) -> Callable:
    @wraps(decored_function)
    async def wrapper(request: Request, response: Response, *args, **kwargs):
        root_route = os.path.dirname(os.path.abspath("main.py"))
        file_route = os.path.join(root_route, "logs.txt")
        with open(file_route, "a") as file:
            file.write(f'[{request["path"]}][200][{request["method"]}]\n')
        return await decored_function(request, response, *args, **kwargs)

    return wrapper
