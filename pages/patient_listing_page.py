from test_QA.pages.base_page import BasePage
from .locators import PatientListingPageLocators
from selenium.webdriver.support import expected_conditions as EC


class PatientListingPage(BasePage):
    def is_patient_listing_page(self):
        assert EC.text_to_be_present_in_element(self.browser.find_element(*PatientListingPageLocators.PAGE_NAME),
                                                PatientListingPageLocators.PAGE_NAME_VALUE)

    def logout(self):
        settings_button = self.browser.find_element(*PatientListingPageLocators.SETTINGS_BUTTON)
        settings_button.click()
        logout_button = self.browser.find_element(*PatientListingPageLocators.LOGOUT_BUTTON)
        logout_button.click()

