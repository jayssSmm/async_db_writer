from pathlib import Path
from fastapi.templating import Jinja2Templates
import os
from dotenv import load_dotenv
import redis
from celery import Celery
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

REDIS_URL = os.getenv('REDIS_URL')
DATABASE_URL = os.getenv('PSQL_URL')

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR/'templates')

redis_client = redis.from_url(REDIS_URL, decode_responses=True)

celery_app = Celery(
    "extensions",
    broker = REDIS_URL,
    backend = None,
) 

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

celery_app.conf.task_ignore_result = True