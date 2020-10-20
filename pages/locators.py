from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, "identification")
    PASSWORD_FIELD = (By.ID, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[type=submit]")
    PAGE_NAME = (By.CSS_SELECTOR, '[class="form-signin"]')


class PatientListingPageLocators:
    PAGE_NAME = (By.CSS_SELECTOR, "[class='view-current-title']")
    PAGE_NAME_VALUE = 'Patient Listing'
    # PATIENT_PAGE = (By.CSS_SELECTOR, '[class="ember-application"]')
    LOGIN_PAGE = (By.CSS_SELECTOR, '[class="ember-application"]')
    SETTINGS_BUTTON = (By.XPATH, '//span[@class="mega-octicon octicon-gear"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[class='logout']")
    MEDICATION_BAR = (By.CSS_SELECTOR, '[href="#/medication"]')
    REQUESTS_PARAGRAPH = (By.CSS_SELECTOR, '[href="#/medication"]')
    COMPLETED_PARAGRAPH = (By.CSS_SELECTOR, '[href="#/medication/completed"]')
    NEW_REQUEST_PARAGRAPH = (By.CSS_SELECTOR, '[href="#/medication/edit/new"]')
    RETURN_MEDICATION_PARAGRAPH = (By.CSS_SELECTOR, '[href="#/medication/return/new"]')
    NEW_REQUEST = (By.CSS_SELECTOR, '[href="#/medication/edit/new"]')
    PATIENT_FIELD = (By.CSS_SELECTOR, '[class="form-control ember-text-field ember-view tt-input"]')
    VISIT_FIELD = (By.CSS_SELECTOR, "[class='form-control ']")
    MEDICATION_FIELD = (By.CSS_SELECTOR, '[class="form-control ember-text-field ember-view tt-input"]')
    PRESCRIPTION_FIELD = (By.CSS_SELECTOR, "[class='form-control  ember-text-area ember-view']")
    QUANTITY_REQUEST_FIELD = (By.CSS_SELECTOR, '[class="form-control  ember-text-field ember-view"]')
    PRESCRIPTION_DATE_FIELD = (By.CSS_SELECTOR, '[class="form-control  ember-text-field ember-view"]')
    REFILS_FIELD = (By.CSS_SELECTOR, '[class="form-control  ember-text-field ember-view"]')
    ADD_BUTTON = (By.XPATH, '//button[text()="Add"]')
    POPUP = (By.CSS_SELECTOR, "[class='modal-body']")
    OK_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-primary on-white "]')
    CROSS_BUTTON = (By.CSS_SELECTOR, "[class='close']")
    POPUP_WINDOW = (By.CSS_SELECTOR, "[class='modal-body']")
    NEW_MEDICATION_REQUEST_PAGE = (By.CSS_SELECTOR, '[class="view-current-title"]')
