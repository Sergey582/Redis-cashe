
from fastapi import FastAPI

from app.api.public import router

app = FastAPI()
app.include_router(router)
