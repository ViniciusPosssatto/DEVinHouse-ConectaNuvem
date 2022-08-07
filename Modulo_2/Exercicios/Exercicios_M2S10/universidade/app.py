from flask.cli import with_appcontext
import click
from src.app import db
from src.app.database import insert_into_DB
from src.app.routes import routes
from src.app import create_app


app = create_app()
routes(app)

@click.command(name='insert')
@with_appcontext
def insert():
    insert_into_DB()


@click.command(name='delete_tables')
@with_appcontext
def delete_tables():
    db.drop_all()


app.cli.add_command(insert)
app.cli.add_command(delete_tables)


if __name__ == '__main__':
    app.run()
