import requests

# print(requests.__file__)
URL = "http://www.google.com"
response = get(URL)

# print(f"Your request to {URL} came back with status code {response.status_code}")