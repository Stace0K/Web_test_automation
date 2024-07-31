# Добавить в наш тестовый проект шаг добавления поста после входа.
# Должна выполняться проверка на наличие названия поста на странице сразу после его создания.


import yaml
from module import Site
import time

with open("testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


def test_created_post(selector_btn, selector_log, selector_passwd, create_btn, s_title, s_descr, s_content, saving,
                      check_post):
    input1 = site.find_element("xpath", selector_log)
    input1.send_keys(testdata['login'])
    input2 = site.find_element("xpath", selector_passwd)
    input2.send_keys(testdata['password'])
    btn = site.find_element("css", selector_btn)
    btn.click()
    btn_create = site.find_element("xpath", create_btn)
    btn_create.click()
    input3 = site.find_element("xpath", s_title)
    input3.send_keys(testdata['title'])
    input4 = site.find_element("xpath", s_descr)
    input4.send_keys(testdata['description'])
    input5 = site.find_element("xpath", s_content)
    input5.send_keys(testdata['content'])
    btn_save = site.find_element("xpath", saving)
    btn_save.click()

    time.sleep(testdata["sleep_time"])

    title_label = site.find_element("xpath", check_post)

    assert title_label.text == testdata["title"], "Test failed"
