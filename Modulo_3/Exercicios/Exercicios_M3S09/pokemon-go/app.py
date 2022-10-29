from src.app import app, mongo_client
from src.app.models.pokemon import create_collection_pokemon
from src.app.models.combat import create_combat_validation
from src.app.routes import routes
from flask.cli import with_appcontext
import click

routes(app)

@click.command(name='create_collections')
@with_appcontext 
def call_command():
    create_combat_validation(mongo_client)
    create_collection_pokemon(mongo_client)


app.cli.add_command(call_command)

if __name__ == "__main__":
    app.run()
