import random
from flask import json


mimetype = 'application/json'
url = "/developers/search_developers"


def test_search_not_authorized(client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    response = client.get(url, headers=headers)
    assert response.status_code == 403
    assert response.json["error"] == "Você não tem permissão"


def test_search_no_content_in_query_param(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"

    response = client.get(url, headers=headers)

    assert response.status_code == 200
    assert "records" in response.json
    assert len(response.json["records"]) >= 0


def test_search_city_id_failed_in_query_param(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"

    query_param = "city_id=fff"

    response = client.get(f"{url}?{query_param}", headers=headers)

    assert response.status_code == 422
    assert response.json["error"] == "City_id não é um número"


def test_search_city_id_in_query_param(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"

    query_param = "city_id=33"

    response = client.get(f"{url}?{query_param}", headers=headers)

    assert response.status_code == 200
    assert "records" in response.json

# TESTE ESTÁ PASSANDO

def test_search_city_id_not_exists_in_query_param(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"

    query_param = "city_id=999999999"
    url = f"/developers/search_developers?{query_param}"
    response = client.get(url, headers=headers)

    assert response.status_code == 200
    assert "records" in response.json
    assert len(response.json["records"])== 0


def test_search_min_max_exp_in_query_param(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"

    query_param1 = "min_exp=33"
    query_param2 = "max_exp=33"

    url = f"/developers/search_developers?{query_param1}&{query_param2}"

    response = client.get(url, headers=headers)

    assert response.status_code == 200
    assert "records" in response.json


def test_search_min_max_exp_failed_in_query_param(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"

    query_param1 = "min_exp=3d3"
    query_param2 = "max_exp=3d3"

    url = f"/developers/search_developers?{query_param1}&{query_param2}"

    response = client.get(url, headers=headers)

    assert response.status_code == 422
    assert response.json["error"] == "Algum dos valores enviados não é um número"


def test_search_accepted_remote_work_in_query_param(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"

    query_param1 = "accepted_remote_work=0"

    url = f"/developers/search_developers?{query_param1}"

    response = client.get(url, headers=headers)

    assert response.status_code == 200
    assert "records" in response.json

def test_search_accepted_remote_work_failed_in_query_param(client, logged_in_client):
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    headers["Authorization"] = f"Bearer {logged_in_client}"

    query_param1 = "accepted_remote_work=444"

    url = f"/developers/search_developers?{query_param1}"

    response = client.get(url, headers=headers)

    assert response.status_code == 422
    assert response.json["error"] == 'accepted_remote_work não é um booleano'

