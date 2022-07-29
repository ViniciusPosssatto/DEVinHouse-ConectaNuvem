from flask import Blueprint


cities = Blueprint('cities', __name__, url_prefix="/city")


@cities.route('/', methods=["GET"])
def list_all_cities():
    return {"data": ["floripa", "eneas", "perola"]}


@cities.route('/', methods=["POST"])
def list_new_cities():
    return {"data": ["floripa", "eneas", "perola"]}