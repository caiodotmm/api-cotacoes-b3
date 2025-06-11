import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()
