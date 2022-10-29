from src.app.utils import read_validator_schema


def create_combat_validation(mongo_client):
    combat_validator = read_validator_schema("validators", "combats")

    try:
        mongo_client.create_collection("combats")

    except Exception as excp:
        print("Erro na model combats: ", excp)

    mongo_client.command("collMod", "combats", validator=combat_validator)
    