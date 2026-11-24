import requests
from jsonschema import validate
from Schemas import get_full_schema


def test_get_list(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}")
    assert response.status_code == 200
    data = response.json()
    validate(data, schema=get_full_schema)

def test_post_user(base_url, endpoint):
    payload = {"title": "Title",
               "body": "Giant text about everything",
               "userId": 1}
    response = requests.post(f"{base_url}{endpoint}", json=payload)
    data = response.json()
    assert response.status_code == 201
    assert payload.items() <= data.items()

def test_update_user(base_url, endpoint):
    payload = {"id": 1,
               "title": "updated",
               "body": "updated body",
               "userId": 1}
    response = requests.put(f"{base_url}{endpoint}/1", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert payload.items() <= data.items()

def test_delete_user(base_url, endpoint):
    response = requests.delete(f"{base_url}{endpoint}/1")
    assert response.json() == {}
    assert response.status_code == 200
