import os
from flask import Flask
from src.config.__init_ import app_config


app = Flask(__name__)

app.config.from_object(app_config[os.getenv('FLASK_ENV')])

@app.route("/teste")
def print():
    data: "2"
    return "<h1>HUEHEE77777777 teste</h1>"
