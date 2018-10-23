from face_config import KEY, BASE_URL
import requests
import json


headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': KEY,
}


def create(person_group_id, person_name):
    url = BASE_URL + '/persongroups/' + person_group_id + '/persons'

    body = {
        "name": person_name
    }

    response = requests.post(url=url, headers=headers, json=body)

    if response.status_code == 200:
        return response.text
    else:
        return response.text


def get_list(person_group_id):
    url = BASE_URL + '/persongroups/' + person_group_id + '/persons'

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return response.text


def add(person_group_id, person_id, image):
    url = BASE_URL + "/persongroups/" + person_group_id + \
        "/persons/" + person_id + "/persistedFaces"

    image_file = open(image, 'rb').read()
    headers['Content-Type'] = 'application/octet-stream'
    response = requests.post(url=url, headers=headers, data=image_file)

    if response.status_code == 200:
        return response.text
    else:
        return response.text


def detect(image):
    url = BASE_URL + "/detect"

    headers['Content-Type'] = 'application/octet-stream'
    response = requests.post(url=url, headers=headers, data=image)

    if response.status_code == 200:
        return response.text
    else:
        return response.text


def identify(person_group_id, face_id):
    url = BASE_URL + "/identify"

    body = {
        "PersonGroupId": person_group_id,
        "faceIds": [face_id],
        "confidenceThreshold": 0.5
    }
    response = requests.post(url=url, headers=headers, json=body)

    if response.status_code == 200:
        return response.text
    else:
        return response.text


def delete(person_group_id, person_id):
    url = BASE_URL + "/persongroups/" + person_group_id + "/persons/" + person_id

    response = requests.delete(url=url, headers=headers)

    if response.status_code == 200:
        return "Success"
    else:
        return response.text
