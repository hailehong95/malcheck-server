import os
from flask import Flask
from minio import Minio
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPDigestAuth

load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
LOGS_DIR = os.path.join(os.path.dirname(BASE_DIR), "logs")
DBS_DIR = os.path.join(os.path.dirname(BASE_DIR), "dbs")
DASH_LOG_FILE = os.path.join(LOGS_DIR, "dash.log")
DASH_DBS_FILE = os.path.join(DBS_DIR, "dash.sqlite")
try:
    for dir_ in [LOGS_DIR, DBS_DIR]:
        if not os.path.exists(dir_):
            os.makedirs(dir_, exist_ok=True)
    for file_ in [DASH_LOG_FILE, DASH_DBS_FILE]:
        if not os.path.isfile(file_):
            open(file_, "a").close()
except Exception as ex:
    pass
app = Flask(__name__, template_folder=TEMPLATES_DIR)
app.app_context().push()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DASH_DBS_FILE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

auth = HTTPDigestAuth()
db = SQLAlchemy(app)

users = {
    os.getenv("DASH_USER"): os.getenv("DASH_PASSWORD")
}

# TELEGRAM
CHAT_ID = os.getenv("CHAT_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# S3/MINIO
MINIO_HOST = os.getenv("MINIO_HOST")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME")
client = Minio(MINIO_HOST, access_key=MINIO_ACCESS_KEY, secret_key=MINIO_SECRET_KEY, )
