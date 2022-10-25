from crypt import methods
import json
from flask import Blueprint
from flask.wrappers import Response


movies = Blueprint("movies", __name__, url_prefix="/movies")


@movies.route("get_all_movies", methods=["GET"])
def get_all_movies():
    return Response(
        response=json.dumps({"records": [
            {"name": "Senhor dos aneis","id": 1},
            {"name": "Fast and furious","id": 2},
            {"name": "Aqueles que não foram","id": 3},
            {"name": "Miranha 2","id": 4},
            {"name": "snake e drake","id": 5}
            ]}),
            status=200,
            mimetype="application/json"
    )