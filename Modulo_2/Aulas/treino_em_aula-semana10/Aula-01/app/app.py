from src.app import create_app


app = create_app()


if __name__ == "__main__":
    app.run()



"""
poetry run flask db init
poetry run flask db migrate
poetry run flask db upgrade
"""