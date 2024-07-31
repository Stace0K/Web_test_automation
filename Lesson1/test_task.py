# Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
# а потом проверяется его наличие на сервере по полю «описание».
# Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts
# с передачей параметров title, description, content.

import requests
import yaml

S = requests.Session()

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    url = data['url_post']


def test_post(login):
    result = S.post(url=url, headers={'X-Auth-Token': login}, data={'title': data['title'],
                                                                    'description': data['description'],
                                                                    'content': data['content']})
    assert result, 'Test 1: failed'


def test_description(login, post_description):
    result = S.get(data['url_post'], params={'description': post_description}, headers={'X-Auth-Token': login})
    assert result, 'Test 2: failed'
