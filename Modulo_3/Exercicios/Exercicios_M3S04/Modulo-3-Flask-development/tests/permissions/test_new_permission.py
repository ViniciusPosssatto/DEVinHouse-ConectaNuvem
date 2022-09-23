from flask import json

mimetype = 'application/json'
url = "/permission/new"


def test_new_permission_authorized(client, logged_in_client):
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype,
		'Authorization': f'Bearer {logged_in_client}'
	}

	data = {
		"description": "Master"
	}

	response = client.post(url, data=json.dumps(data), headers=headers)
	assert response.status_code == 204


def test_new_permission_not_authorized(client):
	headers = {
		'Content-Type': mimetype,
		'Accept': mimetype,
	}
	data = {
		"description": "MASTER"
	}
	response = client.post(url, data=json.dumps(data), headers=headers)
	assert response.status_code == 403


def test_new_permission_failed_exists(client, logged_in_client):
  headers = {
    'Content-Type': mimetype,
    'Accept': mimetype,
    'Authorization': f'Bearer {logged_in_client}'
  }

  data = {
	"description": "WRITE"
  }
  
  response = client.post(url, data=json.dumps(data), headers=headers)
  assert response.status_code == 400
  assert response.json["error"] == "Essa permissão já existe."
