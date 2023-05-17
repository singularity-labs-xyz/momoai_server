from fastapi import FastAPI
from pydantic import BaseModel
from utils import load_env

load_env()

app = FastAPI()

# import routes
from routes import users
from routes import core

# routes
app.include_router(users.router)
app.include_router(core.router)

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

