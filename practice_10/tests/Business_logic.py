import requests


def test_query_parameters(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}?userId=1")
    data = response.json()
    assert all(item.get('userId') == 1 for item in data)