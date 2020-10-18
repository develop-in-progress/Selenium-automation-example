from pages.base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def is_login_page(self):
        assert EC.element_to_be_clickable(self.browser.find_element(*LoginPageLocators.PAGE_NAME))

    def log_in(self, username, password):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys(username)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()
