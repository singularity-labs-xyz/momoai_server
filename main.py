from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.vectorstores import DeepLake
from langchain.embeddings import OpenAIEmbeddings
from bimo_core import DocumentManager, GCSClient, MongoDBClient
from database import db_connection
from dotenv import load_dotenv
import os

# Check for env environment variable
# Load the corresponding .env file
env = os.getenv("ENV", "dev")
load_dotenv(f"config/.env.{env}")
    
# Initialize utility classes
session = db_connection.SessionLocal()
gcs_client = GCSClient(bucket_name="momo-ai")
vector_store = DeepLake(dataset_path="deeplake", embedding_function=OpenAIEmbeddings())
document_manager = DocumentManager(gcs_client=gcs_client, vector_store=vector_store)

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
    from routes import users, chains, documents, schools, tasks, events, courses, assignments
    app.include_router(users.router)
    app.include_router(schools.router)
    app.include_router(courses.router)
    app.include_router(assignments.router)
    app.include_router(events.router)
    app.include_router(tasks.router)
    app.include_router(documents.router)
    # app.include_router(chains.router)


@app.on_event("shutdown")
async def shutdown():
    # await database.disconnect()
    pass

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}
