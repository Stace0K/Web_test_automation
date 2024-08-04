# Добавить в проект тест по проверке механики работы формы Contact Us на главной странице личного кабинета.
# Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.

from testpage import OperationsHelper
import logging
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info('Test 1: starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_passwd('test')
    testpage.login_btn()
    assert testpage.get_error_text() == '401', 'Test 1 FAILED'


def test_contact_us(browser):
    logging.info('Test 2: starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_passwd(testdata['password'])
    testpage.login_btn()
    testpage.contact_btn()
    testpage.enter_your_name(testdata['test_name'])
    testpage.enter_your_email(testdata['test_email'])
    testpage.enter_your_content(testdata['test_content'])
    testpage.contact_us_btn()
    assert testpage.get_alert_msg() == 'Form successfully submitted', 'Test 2 FAILED'
