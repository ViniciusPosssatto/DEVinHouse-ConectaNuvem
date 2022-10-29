from src.app.utils import read_validator_schema


def create_collection_pokemon(mongo_client):
    pokemon_validator = read_validator_schema("validators", "pokemons")

    try:
        mongo_client.create_collection("pokemons")

    except Exception as excp:
        print("Erro na model pokemon: ", excp)

    mongo_client.command("collMod", "pokemons", validator=pokemon_validator)
    