from flask import Flask
import os
from src.app.routes import routes
from src.config.app_config import app_config


app = Flask(__name__)

routes(app)


app.config.from_object(app_config[os.getenv('FLASK_ENV')])


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
