from pages.base_page import BasePage
from .locators import PatientListingPageLocators as PageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date
import time
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select



class PatientListingPage(BasePage):
    def is_patient_listing_page(self):
        assert EC.text_to_be_present_in_element(self.browser.find_element(*PageLocators.PAGE_NAME),
                                                PageLocators.PAGE_NAME_VALUE)

    def logout(self):
        settings_button = self.browser.find_element(*PageLocators.SETTINGS_BUTTON)
        settings_button.click()
        logout_button = self.browser.find_element(*PageLocators.LOGOUT_BUTTON)
        logout_button.click()

    def click_medication_bar(self):
        medication_bar = self.browser.find_element(*PageLocators.MEDICATION_BAR)
        medication_bar.click()

    def check_medication_section(self):
        try:
            requests_paragraph = self.browser.find_elements(*PageLocators.REQUESTS_PARAGRAPH)[1]
            completed_paragraph = self.browser.find_element(*PageLocators.COMPLETED_PARAGRAPH)
            new_request_paragraph = self.browser.find_element(*PageLocators.NEW_REQUEST_PARAGRAPH)
            return_medication_paragraph = self.browser.find_element(*PageLocators.RETURN_MEDICATION_PARAGRAPH)
        except NoSuchElementException:
            assert False, 'At least one medication section missed'

    def click_to_new_request(self):
        new_request = self.browser.find_element(*PageLocators.NEW_REQUEST)
        new_request.click()

    def fill_the_required_forms(self):
        patient_field = self.browser.find_element(*PageLocators.PATIENT_FIELD)
        time.sleep(3)
        patient_field.send_keys('Test Patient', Keys.ARROW_DOWN*4, Keys.ENTER)
        time.sleep(3)

        visit_field = self.browser.find_element(*PageLocators.VISIT_FIELD)
        visit_field.click()
        visit_field = Select(visit_field)
        time.sleep(3)
        visit_field.select_by_index(1)
        time.sleep(4)

        medication_field = self.browser.find_elements(*PageLocators.MEDICATION_FIELD)[1]
        medication_field.send_keys('Pramoxin', Keys.TAB)

        prescription_field = self.browser.find_element(*PageLocators.PRESCRIPTION_FIELD)
        prescription_field.send_keys('Testing prescription ')

        quantity_requested_field = self.browser.find_elements(*PageLocators.QUANTITY_REQUEST_FIELD)[1]
        quantity_requested_field.click()
        quantity_requested_field.send_keys(randint(1, 5))

    def fill_not_the_required_forms(self):
        prescription_date_field = self.browser.find_elements(*PageLocators.PRESCRIPTION_DATE_FIELD)[0]
        prescription_date_field.click()
        prescription_date_field.clear()
        correct_date = date.today().strftime("%m/%d/%Y")
        list_date = correct_date.split('/')
        list_date[1] = str(int(list_date[1]) - 1)
        a_day_earlier = '/'.join(list_date)
        prescription_date_field.send_keys(a_day_earlier)

        refils_field = self.browser.find_elements(*PageLocators.REFILS_FIELD)[2]
        refils_field.click()
        refils_field.send_keys(randint(5, 10))
        time.sleep(3)

    def click_the_add_button(self):
        try:
            add_button = self.browser.find_element(*PageLocators.ADD_BUTTON)
            add_button.click()
        except NoSuchElementException:
            assert False, 'The "Add" button is missed'

    def check_popup_window(self):
        popup = self.browser.find_element(*PageLocators.POPUP)
        assert popup == self.browser.find_element(By.XPATH, '//div[text()="The medication record has been saved."]')

    def check_the_ok_button(self):
        try:
            ok_button = self.browser.find_elements(*PageLocators.OK_BUTTON)[1]
            self.browser.execute_script("arguments[0].scrollIntoView();", ok_button)
        except NoSuchElementException:
            assert False, 'The "Ok" button is missed'

    def check_the_cross_button(self):
        try:
            cross_button = self.browser.find_element(*PageLocators.CROSS_BUTTON)
        except NoSuchElementException:
            assert False, 'The "cross" button is missed'

    def click_the_ok_button(self):
        ok_button = self.browser.find_elements(*PageLocators.OK_BUTTON)[1]
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", ok_button)
        time.sleep(3)
        ok_button.click()

    def check_popup_window_is_not_shown(self):
        try:
            popup_window = self.browser.find_element(*PageLocators.POPUP_WINDOW)
            if popup_window:
                assert False, 'The "popup" window is shown'
        except NoSuchElementException:
            pass

    def user_stayed_on_the_new_medication_request_page(self):
        new_medication_request_page = self.browser.find_element(*PageLocators.NEW_MEDICATION_REQUEST_PAGE)
        assert new_medication_request_page.text == 'New Medication Request'
