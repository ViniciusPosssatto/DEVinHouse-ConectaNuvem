from src.app.controllers.university import university


def routes(app):
    app.register_blueprint(university)
