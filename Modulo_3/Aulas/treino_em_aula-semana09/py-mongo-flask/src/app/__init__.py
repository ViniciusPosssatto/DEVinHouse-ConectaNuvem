import os
from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from src.app.flasgger import create_swagger
from src.app.config import app_config


DB = PyMongo(uri=os.getenv('MONGO_URI'))


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config[os.getenv("FLASK_ENV")])
    create_swagger(app)
    DB.init_app(app)
    CORS
    return app
