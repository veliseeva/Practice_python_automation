import requests


def test_respond_with_keys(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}/1")
    data = response.json()
    assert len(data) > 0
    assert isinstance(data, dict)


def test_empty_json(base_url, endpoint):
    response = requests.delete(f"{base_url}{endpoint}/1")
    assert response.json() == {}
