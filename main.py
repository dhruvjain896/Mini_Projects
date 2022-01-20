import requests
import random
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"


def token_generator():
    alphabets_and_numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    token = ''
    token_len = random.randint(8, 128)
    for i in range(token_len):
        token += random.choice(alphabets_and_numbers)
    return token

# Don't use token_generator() inside code otherwise it will generate new token every time run the code 
# use the function outside to generate the token instead of thinking of one and paste it here.
TOKEN = "YOUR_TOKEN"

# pixela user parameters
user_params = {
    "token": TOKEN,
    "username": "YOUR_USERNAME",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/<your_username>/graphs"

graph_config = {
    "id": "graph1",
    "name": "Studying Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

pixel_endpoint = "https://pixe.la/v1/users/<your_username>/graphs/graph1"

today = datetime.now()

pixel_config = {
    'date': today.strftime('%Y%m%d'),
    "quantity": "5",
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixel_endpoint}/20211122" # Date in YYYYMMDD Format

update_pixel_config = {
    "quantity": "3"
}

response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
print(response.text)

response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)

# Read pixela docs for more info
