from flask import Blueprint, jsonify
from src.app.models.city import City, cities_share_schema

cities = Blueprint('cities', __name__, url_prefix="/city")

@cities.route('/', methods = ["GET"])
def list_all_cities():
  return {"data": ["Javascript", "Python", "Java"]}

@cities.route('/pagina/<int:page_num>', methods = ['GET'])
def list_per_page(page_num):
  cities_ = City.query.paginate(per_page=10, page=page_num, error_out=True)
  ct = cities_share_schema.dump(cities_.items)
  cidads = []
  for item in ct:
    cidads.append(item['name'])
  return jsonify(cidads), 200