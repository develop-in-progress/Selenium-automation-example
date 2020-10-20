from pages.base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

username, password = 'hr.doctor@hospitalrun.io', 'HRt3st12'
invalid_username, invalid_password = '1hr.doct1or@hospitalrun.io', '1HRt3st112'


class LoginPage(BasePage):
    def is_login_page(self):
        try:
            login_link = 'http://demo.hospitalrun.io/#/login'
            by, locator = LoginPageLocators.PAGE_NAME[0], LoginPageLocators.PAGE_NAME[1]
            if WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((by, locator))):
                time.sleep(7)
                assert login_link == self.browser.current_url, 'Page is not the Login page'
        except TimeoutException:
            assert False, 'Page is not the Login page'

    def log_in(self):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys(username)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def log_in_with_invalid_users_data(self):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys(invalid_username)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(invalid_password)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()
