from fastapi import FastAPI

from app.api.public.weather.views import router

app = FastAPI()

app.include_router(router)
