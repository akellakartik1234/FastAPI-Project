import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv(Path(__file__).resolve().parent / ".env")

db_url = os.environ.get("DATABASE_URL")
if not db_url:
    raise RuntimeError(
        "DATABASE_URL is not set. Copy .env.example to .env and set DATABASE_URL, "
        "or export DATABASE_URL in your environment."
    )

engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
