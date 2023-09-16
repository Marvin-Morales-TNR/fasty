from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes.main_route import auth
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
load_dotenv()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth)
