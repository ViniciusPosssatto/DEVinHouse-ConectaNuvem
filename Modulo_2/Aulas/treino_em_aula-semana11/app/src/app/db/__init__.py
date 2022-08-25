from sqlalchemy.sql.expression import func
from flask import json
import requests
from src.app.models.cities import City, cities_share_schema
from src.app.models.country import Country, country_share_schema
from src.app.models.developer import Developer
from src.app.models.state import State, states_share_schema
from src.app.models.technologies  import Technology
from src.app.models.user  import User, users_share_schema


def read():
    try:
        with open('src/app/db/technologies.json', 'r+') as f:
            json_object = json.load(f)
            return json_object
    except:
        return None


def save(data):
    json_object = json.dumps(data, indent=4)
    with open('src/app/db/technologies.json', 'w') as f:
        f.write(json_object)

def populate_db():

    country = Country.query.first()

    if country != None:
        print('Já existe dados populados.')
        return
    brasil_code = 76
    countries_data = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/paises/{brasil_code}")
    states_data = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
    cities_data = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/municipios")

    country_name = countries_data.json()[0]['nome']

    Country.seed(country_name, 'Português')
    country = Country.query.first()
    country_dict = country_share_schema.dump(country)

    for stateObject in states_data.json():
        State.seed(
            country_dict['id'],
            stateObject['nome'],
            stateObject['sigla']
        )

    state = State.query.order_by(State.name.asc()).all()
    state_dict = states_share_schema.dump(state)

    for city_object in cities_data.json():
        state_id = 0
        for state_object in state_dict:
            if state_object['initials'] == city_object['microrregiao']['mesorregiao']['UF']['sigla']:
                state_id = state_object['id']
        City.seed(
            state_id,
            city_object['nome']
        )

    cities = City.query.order_by(City.name.asc()).all()
    cities_dict = cities_share_schema.dump(cities)

    users = requests.get('https://randomuser.me/api?nat=br&results=100')
    techs = requests.get('https://lit-citadel-12163.herokuapp.com/technologies/get_all_technologies')
    
    for tech_object in techs.json():
        Technology.seed(
            tech_object['name']
        )

    for user in users.json()['results']:
        city_id = 2
        for city_object in cities_dict:
            if user['location']['city'] == city_object['name']:
                city_id = city_object['id']
        User.seed(
            city_id,
            user['name']['first'] + ' ' + user['name']['last'],
            user['registered']['age'],
            user['email'],
            user['login']['password']
        )

    users = User.query.order_by(User.name.asc()).all()
    users_dict = users_share_schema.dump(users)

    for index, user_object in enumerate(users_dict):
        if index % 2 == 0:
            techs = Technology.query.order_by(func.random()).limit(10).all()
            Developer.seed(
                None,
                index % 2 == 0,
                user_object['id'],
                techs
            )

    print("Dados inseridos com sucesso.")
    return
