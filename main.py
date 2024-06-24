from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from models import Base
from database import engine


app = FastAPI()

# create all tables in database
Base.metadata.create_all(bind=engine)
