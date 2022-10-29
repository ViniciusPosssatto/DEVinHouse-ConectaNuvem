import os
from flask import Flask
from flask_cors import CORS
from src.app.flasgger import create_swagger
from src.app.config import app_config
from src.app.utils import mongo
from src.app.models.movies import create_collection_movies
from src.app.models.cast import create_collection_cast


app = Flask(__name__)
app.config.from_object(app_config[os.getenv("FLASK_ENV")])

app.config["MONGO_URI"] = os.getenv("MONGO_URI")


create_swagger(app)
mongo.init_app(app)
mongo_client = mongo.cx.get_database("netflix")
# create_collection_cast(mongo_client)
CORS(app)
