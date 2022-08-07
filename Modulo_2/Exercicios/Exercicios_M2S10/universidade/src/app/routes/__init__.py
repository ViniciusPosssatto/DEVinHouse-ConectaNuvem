from flask import Flask
from src.app.controllers.university import university


def routes(app:  Flask):
    app.register_blueprint(university)
