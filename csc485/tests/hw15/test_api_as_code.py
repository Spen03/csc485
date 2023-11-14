import pytest
from csc485.projects.hw15.api import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_strength_by_get(client):
    params = {'password': 'example'}
    response = client.get('/get_strength', query_string=params)
    assert response.status_code == 200
    assert response.json == {'password': 'example', 'strength': 'bad'}


def test_get_strength_by_post(client):
    payload = {'password': 'example'}
    response = client.post('/get_strength', json=payload)
    assert response.status_code == 200
    assert response.json == {'password': 'example', 'strength': 'bad'}


def test_missing_password_key(client):
    payload = {'wrong_key': 'example'}
    response = client.post('/get_strength', json=payload)
    assert response.status_code == 400
    assert response.json == {"error": "Missing key 'password' in the JSON payload"}
