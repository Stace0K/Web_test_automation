from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASSWD_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_ENTER = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_ADD_POST = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_ENTER_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_ENTER_EMAIL = (By.XPATH, """//*[@id = "contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id = "contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_passwd(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_PASSWD_FIELD[1]}')
        passwd_field = self.find_element(TestSearchLocators.LOCATOR_PASSWD_FIELD)
        passwd_field.clear()
        passwd_field.send_keys(word)

    def login_btn(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_enter_login(self):
        enter_field = self.find_element(TestSearchLocators.LOCATOR_ENTER, time=2)
        text = enter_field.text
        logging.info(f'We find text {text} in login field {TestSearchLocators.LOCATOR_ENTER[1]}')
        return text

    def add_post(self):
        logging.info('Click add post button')
        self.find_element(TestSearchLocators.LOCATOR_ADD_POST).click()

    def add_title(self, title):
        time.sleep(2)
        logging.info(f"Send '{title}' to element {TestSearchLocators.LOCATOR_TITLE_POST[1]}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_POST)
        title_field.clear()
        title_field.send_keys(title)

    def add_description(self, description):
        logging.info(f"Send '{description}' to element {TestSearchLocators.LOCATOR_DESCRIPTION_POST[1]}")
        descr_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_POST)
        descr_field.clear()
        descr_field.send_keys(description)

    def add_content(self, content):
        logging.info(f"Send '{content}' to element {TestSearchLocators.LOCATOR_CONTENT_POST[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_POST)
        content_field.clear()
        content_field.send_keys(content)

    def save_post(self):
        logging.info('Click save post button')
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST).click()

    def contact_btn(self):
        logging.info('Click Contact button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT).click()

    def enter_your_name(self, name):
        logging.info(f'Send {name} to element {TestSearchLocators.LOCATOR_ENTER_NAME[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_ENTER_NAME)
        login_field.clear()
        login_field.send_keys(name)

    def enter_your_email(self, email):
        logging.info(f'Send {email} to element {TestSearchLocators.LOCATOR_ENTER_EMAIL[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_ENTER_EMAIL)
        login_field.clear()
        login_field.send_keys(email)

    def enter_your_content(self, content):
        logging.info(f'Send {content} to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        login_field.clear()
        login_field.send_keys(content)

    def contact_us_btn(self):
        logging.info('Click Contact button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def get_alert_txt(self):
        alert = self.driver.switch_to.alert
        message = alert.text
        alert.accept()
        return message

    def get_alert_msg(self):
        time.sleep(2)
        logging.info('Get alert message')
        txt = self.get_alert_txt()
        logging.info(f'Alert message is {txt}')
        return txt

