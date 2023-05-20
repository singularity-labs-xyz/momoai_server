import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from utils import load_env

load_env()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    # Define utility classes
    global mongo
    global gcs
    global document_manager

    # Initialize utility classes
    from momoai_core import DocumentManager, GCSClient, MongoDBClient
    mongo = MongoDBClient(os.getenv("MONGO_HOST"), int(os.getenv("MONGO_PORT")), username=os.getenv("MONGO_USER"), password=os.getenv("MONGO_PASSWORD"), db_name=os.getenv("DB"))
    vector_store = DeepLake(dataset_path="deeplake", embedding_function=OpenAIEmbeddings())
    gcs_client = GCSClient(bucket_name="momo-ai")
    document_manager = DocumentManager(gcs_client=gcs_client, vector_store=vector_store)

    # Mount routes
    from routes import user, chain
    app.include_router(user.router)
    app.include_router(chain.router)

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

