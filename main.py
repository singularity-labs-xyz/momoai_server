from fastapi import FastAPI
from utils import load_env


app = FastAPI()

# Load environment
load_env()

# Import managers
from momoai_core import ChainManager, DocumentManager

# Init utility classes
global chain_manager
global document_manager

chain_manager = ChainManager()
document_manager = DocumentManager()

# Import routes
from routes import users
from routes import core

# Mount routes
app.include_router(users.router)
app.include_router(core.router)

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

