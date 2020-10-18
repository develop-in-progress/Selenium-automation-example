from .pages.login_page import LoginPage
from .pages.patient_listing_page import PatientListingPage
import pytest
import time

link = "http://demo.hospitalrun.io/"
username, password = 'hr.doctor@hospitalrun.io', 'HRt3st12'
invalid_username, invalid_password = '1hr.doct1or@hospitalrun.io', '1HRt3st112'



@pytest.mark.main_task
class TestMain:
    def test_user_can_log_in(self, browser):  # User can login with correct credentials
        page = LoginPage(browser, link)
        page.open()
        page.log_in(username, password)
        patient_listing_page = PatientListingPage(browser, browser.current_url)
        patient_listing_page.is_patient_listing_page()

    def test_user_cant_log_in(self, browser):  # User can`t login with invalid credentials
        page = LoginPage(browser, link)
        page.open()
        page.log_in(invalid_username, invalid_password)
        page.is_login_page()

    def test_able_to_logout(self, browser):  # User is able to logout
        page = LoginPage(browser, link)
        page.open()
        page.log_in(username, password)
        patient_listing_page = PatientListingPage(browser, browser.current_url)
        patient_listing_page.logout()
        login_page = LoginPage(browser, browser.current_url)
        login_page.is_login_page()
