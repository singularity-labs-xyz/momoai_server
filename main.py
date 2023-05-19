import os

from fastapi import FastAPI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from utils import load_env

# Load Environment
load_env()

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Define utility classes
    global mongo
    global gcs
    global document_manager

    # Initialize utility classes
    from momoai_core import DocumentManager, GCSClient, MongoDBClient
    mongo = MongoDBClient(os.getenv("MONGO_HOST"), int(os.getenv("MONGO_PORT")), username=os.getenv("MONGO_USER"), password=os.getenv("MONGO_PASSWORD"), db_name=os.getenv("DB"))
    deeplake = DeepLake(dataset_path="deeplake", embedding_function=OpenAIEmbeddings())
    gcs = GCSClient(os.getenv("GCS_BUCKET"))
    document_manager = DocumentManager(gcs=gcs, vector_store=deeplake)

    # Mount routes
    from routes import users, core
    app.include_router(users.router)
    app.include_router(core.router)

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

