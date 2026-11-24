import requests



def test_get_existing_post(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}/1")
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1
    assert all(key in data for key in ['userId', 'id', 'title', 'body'])

def test_get_unexisting_post(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}/99999")
    assert response.status_code == 404
    assert response.json() == {}
