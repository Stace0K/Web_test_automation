# Добавить в проект тесты API, написанные в ходе первого семинара.
# Доработать эти тесты в едином стиле с тестами UI, добавив логирование и обработку ошибок.
# Должен получиться единый тестовый проект.


import logging
import requests
import yaml


with open('testdata.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


S = requests.Session()


def test_create_post(login):
    logging.info('Test Create post: running')
    res = S.post(url=data['posts'], headers={'X-Auth-Token': login},
                 data={'title': data['title'], 'description': data['description'], 'content': data['content']})
    logging.debug(f'Response is {str(res)}')
    assert str(res) == '<Response [200]>', 'Test Create post FAILED'


def test_check_post(login):
    logging.info('Test Check post: running')
    result = S.get(url=data['api'], headers={'X-Auth-Token': login}).json()['data']
    logging.debug(f'Get request returned: {result}')
    list_description = [i['description'] for i in result]
    assert data['description'] in list_description, 'Test Check post FAILED'


def test_not_me_post(login):
    logging.info('Test Not me post: running')
    result = S.get(url=data['api'], headers={'X-Auth-Token': login}, params={'owner': 'notMe'}).json()[
        'data']
    print(result)
    logging.debug(f'Get request returned: {result}')
    res_title = [i['title'] for i in result]
    print(res_title)
    assert data['not_me_title'] in res_title, 'Test Not me post FAILED'
