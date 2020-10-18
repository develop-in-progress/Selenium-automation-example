from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, "identification")
    PASSWORD_FIELD = (By.ID, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[type=submit]")
    PAGE_NAME = (By.CSS_SELECTOR, '[class="form-signin"]')


class PatientListingPageLocators:
    PAGE_NAME = (By.CSS_SELECTOR, "[class='view-current-title']")
    PAGE_NAME_VALUE = 'Patient Listing'
    SETTINGS_BUTTON = (By.XPATH, '//span[@class="mega-octicon octicon-gear"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[class='logout']")
