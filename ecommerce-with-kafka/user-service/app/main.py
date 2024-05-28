from fastapi import FastAPI
from app.routes.user_routes import router

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to User Service"

app.include_router(router=router)