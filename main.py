from fastapi import FastAPI
from pydantic import BaseModel

import os
from dotenv import load_dotenv

env = os.getenv("ENV", "dev")

if env == "dev":
    load_dotenv("config/.env.dev")
elif env == "prod":
    load_dotenv("config/.env.prod")
else:
    raise Exception(f"Unknown environment {env}")

from momoai_core.src import managers
from momoai_core.src.chains import *

chain_manager = managers.ChainManager()

app = FastAPI()

class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

@app.get("/test")
async def test():
    return(chain_manager.default_chains["llm"].run("respond with hello."))


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}