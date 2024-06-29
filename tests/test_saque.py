import json
from http.client import BAD_REQUEST, OK

import requests


def test_endpoint_should_return_200_when_valid_value_request():
    payload = get_payload(300)
    headers = get_default_headers()
    url = get_url()
    response = requests.post(url=url, json=payload, headers=headers)
    assert response.status_code == OK


def test_endpoint_should_return_serialized_data_when_valid_value_request():
    from services.ATM.main import get_available_ballots_value
    payload = get_payload(100)
    headers = get_default_headers()
    url = get_url()
    response = requests.post(url=url, json=payload, headers=headers)
    for nota in get_available_ballots_value():
        assert str(nota) in response.json()
    assert response.status_code == OK


def test_endpoint_should_return_400_when_receive_negative_value():
    payload = get_payload(-1)
    headers = get_default_headers()
    url = get_url()
    response = requests.post(url=url, json=payload, headers=headers)
    assert response.status_code == BAD_REQUEST


def test_endpoint_should_return_400_when_receive_float_value():
    payload = get_payload(0.9)
    headers = get_default_headers()
    url = get_url()
    response = requests.post(url=url, json=payload, headers=headers)
    assert response.status_code == BAD_REQUEST


def test_endpoint_should_return_400_when_receive_value_one():
    payload = get_payload(1)
    headers = get_default_headers()
    url = get_url()
    response = requests.post(url=url, json=payload, headers=headers)
    assert response.status_code == BAD_REQUEST


def get_payload(value: int | float):
    return {"valor": value}


def get_url():
    base_url = 'http://localhost:5000/'
    return base_url + 'api/saque'


def get_default_headers():
    return {
        'Content-Type': 'application/json'
    }
