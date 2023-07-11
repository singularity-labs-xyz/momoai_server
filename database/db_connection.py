import os
from sqlalchemy import create_engine, Enum
from sqlalchemy.orm import sessionmaker
import database.models
from sqlalchemy.dialects.postgresql import ENUM


engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)