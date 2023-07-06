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
    global gcs_client
    global document_manager
    global session

    # Initialize utility classes
    from momoai_core import DocumentManager, GCSClient, MongoDBClient
    mongo = MongoDBClient(os.getenv("MONGO_HOST"), int(os.getenv("MONGO_PORT")), username=os.getenv("MONGO_USER"), password=os.getenv("MONGO_PASSWORD"), db_name=os.getenv("DB"))
    vector_store = DeepLake(dataset_path="deeplake", embedding_function=OpenAIEmbeddings())
    gcs_client = GCSClient(bucket_name="momo-ai")
    document_manager = DocumentManager(gcs_client=gcs_client, vector_store=vector_store)
    from database import db_connection
    session = db_connection.SessionLocal()

    # Mount routes
    from routes import users, chains, documents, schools, tasks, events, courses, assignments
    app.include_router(users.router)
    app.include_router(schools.router)
    app.include_router(chains.router)
    app.include_router(documents.router)
    app.include_router(tasks.router)
    app.include_router(events.router)
    app.include_router(courses.router)
    app.include_router(assignments.router)


@app.on_event("shutdown")
async def shutdown():
    pass
    # await database.disconnect()

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

