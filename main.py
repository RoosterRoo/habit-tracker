import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = 'https://pixe.la/v1/users'

TOKEN = os.environ.get('TOKEN')
USERNAME = os.environ.get('USERNAME')

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

headers = {
    "X-USER-TOKEN": TOKEN
}

GRAPH_ID = "code-graph"
graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Tracker",
    "unit": "days",
    "type": "int",
    "color": "sora"
}

# response = requests.post(url=f'{pixela_endpoint}/{USERNAME}/graphs', json=graph_params, headers=headers)
# print(response.text)

# today = datetime.now().strftime('%Y%m%d')

yesterday = "20230410"

pixel_params = {
    "date": str(yesterday),
    "quantity": "2"
}

# Posting a pixel
# response = requests.post(url=f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}', json=pixel_params, headers=headers)
# print(response.text)

response = requests.get(url=f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}', headers=headers)

with open('graph.svg', 'a') as file:
    file.write(response.text)

# print(response.text)



