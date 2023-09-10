from fastapi import FastAPI
from .routes import prediction

app = FastAPI()

app.include_router(prediction.router)
