import requests
from requests.auth import HTTPBasicAuth
from werkzeug.security import generate_password_hash
import pytest
from server import app
from multiprocessing import Process

TEST_URL = "http://127.0.0.1:5000/rest/List"
username2 = 'user2'
password2 = 'password2'
username1 = 'user1'
password1= 'password1'

# Issues with this, so turned it off for now.

# @pytest.fixture(scope='module')
# def start_flask_server():
#     process = Process(target=app.run, kwargs={'debug': True})
#     process.start()
#     yield
#     process.terminate()

# This is a dummy test just to check the web server up and running
def test_home_page():
    response = requests.get("http://127.0.0.1:5000/", auth=HTTPBasicAuth(username1, password1))

    assert response.status_code == 200
    assert response.json()['message'] == "Hello world"


# Check user can access a country they are allowed to
def test_check_allowed_country():
    params = {
        'countryCode': 'DE',
        'languageCode': 'de',
        'searchText': 'Hallo Deutschland über Straße'
    }
    response = requests.get(TEST_URL, params=params, auth=HTTPBasicAuth(username1, password1))

    assert response.status_code == 200
    ret_msg = "The server found this message " + params['searchText']
    assert response.json()['message'] == ret_msg


# Check user CANNOT access a country they are NOT allowed to
def test_check_allowed_country():
    params = {
    'countryCode': 'IN',
    'languageCode': 'en',
    'searchText': 'hello india'
    }
    response = requests.get(TEST_URL, params=params, auth=HTTPBasicAuth(username1, password1))

    assert response.status_code == 403

# test a unlogged in user gets an error
def test_unlogged_in_user():
    response = requests.get(TEST_URL)

    assert response.status_code == 401

# test Russia is forbidden
def test_Russia_not_allowed():
    params = {
    'countryCode': 'RU',
    'languageCode': 'en',
    'searchText': 'hello india'
    }
    response = requests.get(TEST_URL, params=params, auth=HTTPBasicAuth(username1, password1))

    assert response.status_code == 403

# check a country not in the list
def test_non_existent_country():
    params = {
    'countryCode': 'XX',
    'languageCode': 'en',
    'searchText': 'hello india'
    }
    response = requests.get(TEST_URL, params=params, auth=HTTPBasicAuth(username1, password1))

    assert response.status_code == 403

# check with a user who doesnt exist
def test_user_not_exist():
    response = requests.get(TEST_URL, auth=HTTPBasicAuth("unknown", password1))

    assert response.status_code == 401
