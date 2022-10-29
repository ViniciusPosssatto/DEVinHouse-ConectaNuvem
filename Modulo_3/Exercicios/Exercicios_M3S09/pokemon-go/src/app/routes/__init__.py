from flask import Flask
from src.app.controllers.pokemon_routes import pokemons

def routes(app: Flask):
  app.register_blueprint(pokemons)
