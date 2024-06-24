from sqlalchemy import create_engine
from sqlalchemy.types import JSON
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from os import getenv
from typing import Any

SQLALCHEMY_DATABASE_URL = getenv("DB_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    type_annotation_map = {
        dict[str, Any]: JSON
    }
