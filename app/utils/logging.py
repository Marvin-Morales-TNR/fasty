import os
from typing import Callable
from fastapi import Request, Response

class Loggin(object):
   def log_request(self, route: str, method: str, status: int, msg: str) -> None:
      root_route = os.path.dirname(os.path.abspath("main.py"))
      file_route = os.path.join(root_route, "logs.txt")
      with open(file_route, "w") as file:
         file.write(f'[{route}][{status}][{method}]: {msg}\n')
