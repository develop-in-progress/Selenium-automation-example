from pages.login_page import LoginPage
from pages.patient_listing_page import PatientListingPage
import pytest
import allure
from allure_commons.types import AttachmentType

link = "http://demo.hospitalrun.io/"


# Main task
@allure.severity('blocker')
@allure.feature('Login and loguot tests')
@pytest.mark.main_task
class TestMain:
    @allure.story('User can login with correct credentials')
    def test_user_can_log_in(self, browser):  # User can login with correct credentials
        page = LoginPage(browser, link)
        with allure.step('Логинимся с валидными данными'):
            allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        page.open()
        page.log_in()
        patient_listing_page = PatientListingPage(browser, browser.current_url)
        patient_listing_page.is_patient_listing_page()

    @allure.story('User can`t login with invalid credentials')
    def test_user_cant_log_in_with_invalid_users_data(self, browser):  # User can`t login with invalid credentials
        page = LoginPage(browser, link)
        page.open()
        page.log_in_with_invalid_users_data()
        page.is_login_page()

    @allure.story('User is able to logout')
    def test_user_is_able_to_logout(self, browser):  # User is able to logout
        page = LoginPage(browser, link)
        page.open()
        page.log_in()
        patient_listing_page = PatientListingPage(browser, browser.current_url)
        patient_listing_page.logout()
        login_page = LoginPage(browser, browser.current_url)
        login_page.is_login_page()


# Additional task
@allure.severity('blocker')
@pytest.mark.additional_task
class TestAdditional:
    @allure.story('User can order medication')
    def test_user_can_log_in_and_order_medication(self, browser):  # User can order medication
        page = LoginPage(browser, link)
        page.open()
        page.log_in()
        patient_listing_page = PatientListingPage(browser, browser.current_url)
        patient_listing_page.is_patient_listing_page()
        patient_listing_page.click_medication_bar()
        patient_listing_page.check_medication_section()
        patient_listing_page.click_to_new_request()
        patient_listing_page.fill_the_required_forms()
        patient_listing_page.fill_the_not_required_forms()
        patient_listing_page.click_the_add_button()
        patient_listing_page.check_popup_window()
        patient_listing_page.check_the_ok_button()
        patient_listing_page.check_the_cross_button()
        patient_listing_page.click_the_ok_button()
        patient_listing_page.check_popup_window_is_not_shown()
        patient_listing_page.user_stayed_on_the_new_medication_request_page()
