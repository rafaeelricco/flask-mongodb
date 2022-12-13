import os
from flask import Flask
from dotenv import load_dotenv
from flask_pymongo import MongoClient

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)

# Connect to MongoDB
mongo = MongoClient(os.getenv("MONGO_URI"))
db = mongo.get_default_database(os.getenv("MONGO_DBNAME"))
collection = db.get_collection(os.getenv("MONGO_COLLECTION"))

# Create Flask app and register blueprints
def create_app():
    app = Flask(__name__)

    from app.api.base import api_todos

    app.register_blueprint(api_todos)

    return app
