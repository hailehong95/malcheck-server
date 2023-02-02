import os

from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MINIO
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MINIO_HOST = os.getenv("MINIO_HOST")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_SERVICE_LOG_FILE = os.path.join(DATA_DIR, "minio-api.log")
