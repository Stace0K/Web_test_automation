from testpage import OperationsHelper
import logging
import yaml
import time

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_error(browser):
    logging.info('Test Error: running')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_passwd('test')
    testpage.login_btn()
    assert testpage.get_error_text() == '401', 'Test Error FAILED'


def test_log_in(browser):
    logging.info('Test Enter: running')
    testpage = OperationsHelper(browser)
    testpage.enter_login(testdata['login'])
    testpage.enter_passwd(testdata['password'])
    testpage.login_btn()
    assert testpage.get_enter_login() == f'Hello, {testdata["login"]}', 'Test Log in FAILED'


def test_title(browser):
    logging.info('Test Title: running')
    testpage = OperationsHelper(browser)
    testpage.new_post_btn()
    testpage.add_title(testdata['title'])
    testpage.add_description(testdata['description'])
    testpage.add_content(testdata['content'])
    testpage.save_post()
    time.sleep(2)
    assert testpage.get_label() == testdata['title'], 'Test Title FAILED'


def test_contact_us(browser):
    logging.info('Test Contact us: running')
    testpage = OperationsHelper(browser)
    testpage.contact_btn()
    testpage.enter_your_name(testdata['test_name'])
    testpage.enter_your_email(testdata['test_email'])
    testpage.enter_your_content(testdata['test_content'])
    testpage.contact_us_btn()
    assert testpage.get_alert_msg() == 'Form successfully submitted', 'Test Contact us FAILED'


