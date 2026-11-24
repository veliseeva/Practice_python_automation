import requests


def test_200_ok(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}")
    assert response.status_code == 200

def test_201_created(base_url, endpoint):
    payload = {"title": "Title",
               "body": "Giant text about everything",
               "userId": 1}
    response = requests.post(f"{base_url}{endpoint}", json=payload)
    assert response.status_code == 201

def test_404_not_found(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}/unexpected_id")
    assert response.status_code == 404

def test_500_internal_server_error(base_url, endpoint):
    payload = 999999
    response = requests.post(f"{base_url}{endpoint}", json=payload)
    assert response.status_code == 500

