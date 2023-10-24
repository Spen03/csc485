import json
import pytest
# from path-to-the-api-code.api import app  # this is the flask app
from csc485.projects.hw14.api import app


# this is a pytest fixture
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# this is a simplified happy path hw14
def test_expect_good(client):
    # call the API, get the server response
    response = client.get('/get_strength?password=%%%%%%%')
    assert response.status_code == 200

    # convert the json payload to a dict
    data = json.loads(response.data.decode())

    assert data.get('password') == '%%%%%%%'
    assert data.get('strength') == 'good'


# this is an example very negative hw14
def test_api_error(client):
    # disambiguate
    password = '#password'

    with pytest.raises(ZeroDivisionError):
        response = client.get(f"/get_strength?password={password}")
