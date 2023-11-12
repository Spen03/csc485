import json
import pytest
# from path-to-the-api-code.api import app  # this is the flask app
from csc485.projects.hw14.api import app

"""
*
"""


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
        assert response.status_code == 200


@pytest.mark.parametrize('call_response', {
    ('a' * 100 + '%' * 0, 'bad'),
    ('a' * 99 + '%' * 1, 'bad'),
    ('a' * 90 + '%' * 10, 'bad'),
    ('a' * 51 + '%' * 49, 'bad'),
    ('a' * 50 + '%' * 50, 'bad'),
    ('a' * 49 + '%' * 51, 'good'),
    ('a' * 1 + '%' * 99, 'good'),
    ('a' * 0 + '%' * 100, 'good')
})
def test_paramaterize_call_response(client, call_response):
    password, expected_strength = call_response
    response = client.get('/get_strength?password=' + password)
    assert response.status_code == 200

    # convert the json payload to a dict
    data = json.loads(response.data.decode())

    # assert not len(data.get('password')) == len(password)

    assert data.get('password') == password
    assert data.get('strength') == expected_strength


@pytest.mark.parametrize('bad_value_password', {
    ('%%%%%%%%abc', 'good'),  # bad because of escape ...%%abc... => ...%%ABcabc...
})
def test_escape_inequal(client, bad_value_password):
    password, expected_strength = bad_value_password
    response = client.get('/get_strength?password=' + password)
    assert response.status_code == 200

    # convert the json payload to a dict
    data = json.loads(response.data.decode())

    assert len(data.get('password')) == len(password)  # why is this working now?

    # assert data.get('password') == password
    assert data.get('strength') == expected_strength
