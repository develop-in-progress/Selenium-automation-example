from pages.base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

username, password = 'hr.doctor@hospitalrun.io', 'HRt3st12'
invalid_username, invalid_password = '1hr.doct1or@hospitalrun.io', '1HRt3st112'


class LoginPage(BasePage):
    def is_login_page(self):
        try:
            self.browser.find_element(*LoginPageLocators.PAGE_NAME)
        except NoSuchElementException:
            return False
        return True

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