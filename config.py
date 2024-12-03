from dotenv import load_dotenv
import os

# Specify the .env file explicitly
load_dotenv("dev.env")


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    DEBUG = os.getenv("FLASK_ENV") == "development"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
