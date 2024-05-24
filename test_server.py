import requests
from requests.auth import HTTPBasicAuth
from werkzeug.security import generate_password_hash

TEST_URL = "http://127.0.0.1:5000/rest/List"
params = {
    'countryCode': 'IN',
    'languageCode': 'en',
    'searchText': 'hello india'
}

# Define the username and password
username = 'user2'
password = 'password2'



# Make the GET request with basic authentication
response = requests.get(TEST_URL, params=params, auth=HTTPBasicAuth(username, password))

print('Status Code:', response.status_code)
print('Response JSON:', response.json())

params = {
    'countryCode': 'DE',
    'languageCode': 'de',
    'searchText': 'Hallo Deutschland über Straße'
}

# Define the username and password
username = 'user1'
password = 'password1'

# hashed_password = generate_password_hash(password)

# Make the GET request with basic authentication
response = requests.get(TEST_URL, params=params, auth=HTTPBasicAuth(username, password))

print('Status Code:', response.status_code)
print('Response JSON:', response.json())