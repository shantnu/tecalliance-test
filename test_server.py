import requests

TEST_URL = "http://127.0.0.1:5000"

response = requests.get(TEST_URL)

print('Status Code:', response.status_code)
print('Response JSON:', response.json())