import pytest
import requests
import random
import string

from data import CommonData


@pytest.fixture
def create_user():
    letters = string.ascii_lowercase
    login = ''.join(random.choice(letters) for _ in range(10)) + '@ya.ru'
    payload = {"email": f'{login}',
               "password": CommonData.test_user_password,
               "name": CommonData.test_user_name
               }
    response = requests.post(CommonData.register_url, data=payload)
    access_token = ''
    if response.status_code == 200:
        access_token = response.json().get("accessToken")
    yield response, login, access_token
    headers = {'Authorization': f'{access_token}'}
    requests.delete(CommonData.delete_user_url, headers=headers)


@pytest.fixture
def create_fifty_one_orders(create_user):
    payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}
    headers = {'Authorization': f'{create_user[2]}'}
    for order in range(51):
        requests.post(CommonData.create_order_url, data=payload, headers=headers)


@pytest.fixture
def create_three_orders(create_user):
    payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}
    headers = {'Authorization': f'{create_user[2]}'}
    for order in range(3):
        requests.post(CommonData.create_order_url, data=payload, headers=headers)
