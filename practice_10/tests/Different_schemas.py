import requests
from jsonschema import validate
from Schemas import get_full_schema, get_list_item_schema, empty_schema, create_response_schema


def test_list_of_posts(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}")
    assert response.status_code == 200
    data = response.json()
    validate(data, schema=get_full_schema)

def test_list_item(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}/1")
    assert response.status_code == 200
    data = response.json()
    validate(data, schema=get_list_item_schema)

def test_empty(base_url, endpoint):
    response = requests.delete(f"{base_url}{endpoint}/1")
    assert response.status_code == 200
    data = response.json()
    validate(data, schema=empty_schema)

def test_create_item(base_url, endpoint):
    payload = {"title": "Title",
               "body": "Giant text about everything",
               "userId": 1}
    response = requests.post(f"{base_url}{endpoint}", json=payload)
    data = response.json()
    assert response.status_code == 201
    validate(data, schema=create_response_schema)