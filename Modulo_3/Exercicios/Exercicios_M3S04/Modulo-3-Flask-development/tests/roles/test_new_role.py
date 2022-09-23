from flask import json


mimetype = 'application/json'
url = "/role/new"


def test_new_role_authorized(client, logged_in_client):
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype,
		'Authorization': f'Bearer {logged_in_client}'
	}

	data = {
		"description": "ADMIN",
		"permissions": [
			{id: 1}, {id: 2}, {id: 3}
		]
	}

	response = client.post(url, data=json.dumps(data), headers=headers)
	assert response.status_code == 204


def test_new_role_not_authorized(client):
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype,
	}
	data = {
		"description": "ADMIN"
	}

	response = client.post(url, data=json.dumps(data), headers=headers)
	assert response.status_code == 403 
	assert response.json["error"] == "Você não tem permissão para isso"


def test_new_role_failed_exists(client, logged_in_client):
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype,
		'Authorization': f'Bearer {logged_in_client}'
	}

	data = {
		"description": "ADMIN"
	}

	response = client.post(url, data=json.dumps(data), headers=headers)
	assert response.status_code == 400
	assert response.json["error"] == "Esse cargo já existe"


def test_new_role_failed_exists(client, logged_in_client):
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype,
		'Authorization': f'Bearer {logged_in_client}'
	}

	data = {
		"description": "ADMIN",
		"permissions": [
			{id: 1}, {id: 2}, {id: 3}
		]
	}

	response = client.post(url, data=json.dumps(data), headers=headers)
	assert response.status_code == 400
	assert response.json["error"] == "Esse cargo já existe"


def test_new_role_permission_not_exists(client, logged_in_client):
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype,
		'Authorization': f'Bearer {logged_in_client}'
	}

	data = {
		"description": "ADMIN",
		"permissions": [
			{id: 99999}
		]
	}

	response = client.post(url, data=json.dumps(data), headers=headers)
	assert response.status_code == 400
	assert response.json["error"] == "Esse cargo já existe"