import yaml
import pytest

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def selector_log():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def selector_passwd():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def selector_err():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def selector_btn():
    return """button"""


@pytest.fixture()
def selector_hpg():
    return """//*[@id="app"]/main/nav/a/span"""


@pytest.fixture()
def create_btn():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def s_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def s_descr():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def s_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def saving():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def check_post():
    return """//*[@id="app"]/main/div/div[1]/h1"""
