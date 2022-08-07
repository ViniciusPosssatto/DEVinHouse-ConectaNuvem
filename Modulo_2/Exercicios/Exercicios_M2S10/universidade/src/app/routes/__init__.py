from re import A
from flask import Flask
from src.app.controllers.alunos_routes import alunos_route


def routes(app:  Flask):
    app.register_blueprint(alunos_route)
