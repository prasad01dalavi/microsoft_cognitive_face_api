from face_config import KEY, BASE_URL
import requests
import json


headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': KEY,
}


def create(person_group_id, group_name):
    url = BASE_URL + '/persongroups/' + person_group_id

    body = {
        "name": group_name
    }

    response = requests.put(url=url, headers=headers, json=body)

    if response.status_code == 200:
        return "Group Created!"
    else:
        return response.text


def info(person_group_id):
    url = BASE_URL + '/persongroups/' + person_group_id
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return response.text


def train(person_group_id):
    url = BASE_URL + "/persongroups/" + person_group_id + "/train"

    response = requests.post(url=url, headers=headers)

    if response.status_code == 202:
        return "Success!"
    else:
        return response.text


def training_status(person_group_id):
    url = BASE_URL + "/persongroups/" + person_group_id + "/training"

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return response.text


def delete(person_group_id):
    url = BASE_URL + "/persongroups/" + person_group_id

    response = requests.delete(url=url, headers=headers)

    if response.status_code == 200:
        return "Success"
    else:
        return response.text
