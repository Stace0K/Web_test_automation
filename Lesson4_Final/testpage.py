import time
import logging
import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    ids = dict()
    with open('./locators.yaml', encoding='utf-8') as f:
        locators = yaml.safe_load(f)

    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get test from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login form')

    def enter_passwd(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASSWD_FIELD'], word, description='pasword form')

    def add_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_TITLE_POST'], word, description='title form')

    def add_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_DESCRIPTION_POST'], word,
                                   description='description form')

    def add_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT_POST'], word, description='content form')

    def enter_your_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_ENTER_NAME'], word, description='contact name form')

    def enter_your_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_ENTER_EMAIL'], word,
                                   description='contact email form')

    def enter_your_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT_FIELD'], word,
                                   description='contact content form')

    # CLICK
    def login_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='login')

    def contact_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT'], description='contact')

    def contact_us_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_US_BTN'], description='contact us')

    def new_post_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_NEW_POST_BTN'], description='new post button')

    def save_post(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_SAVE_POST'], description='save')

    # GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], description='error')

    def get_enter_login(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ENTER'], description='login')

    def get_label(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_LABEL'], description='label')

    def get_alert_txt(self):
        alert = self.driver.switch_to.alert
        message = alert.text
        alert.accept()
        return message

    def get_alert_msg(self):
        time.sleep(1)
        logging.info('Get alert message')
        txt = self.get_alert_txt()
        logging.info(f'Alert message is {txt}')
        return txt
