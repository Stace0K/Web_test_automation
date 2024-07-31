import pytest
import requests
import yaml


with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username, password, url_log = data['username'], data['password'], data['url_log']


S = requests.Session()


@pytest.fixture()
def login():
    result = S.post(url=url_log, data={'username': username, 'password': password})
    return result.json()['token']


@pytest.fixture()
def post_description():
    return 'MaruTalks is here'
