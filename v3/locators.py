from selenium.webdriver.common.by import By

class BasePageLocators(object):
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")


class PageOneLocators(object):
    FIRST_NAME = (By.NAME, "fname")
    LAST_NAME = (By.NAME, "lname")
    EMAIL = (By.NAME, "email")
    ZIP = (By.NAME, "zip")


class PageTwoLocators(object):
    ADDRESS1 = (By.NAME, "address1")
    CITY = (By.NAME, "city")
    STATE = (By.NAME, "state")
    LIVED_MORE_SIX_MONTHS_YES = (By.CSS_SELECTOR, "input[name='lived_more_six_months'][value='yes']")
    LIVED_MORE_SIX_MONTHS_NO = (By.CSS_SELECTOR, "input[name='lived_more_six_months'][value='no']")
    PHONE1 = (By.NAME, "phone1")
    SSN1 = (By.NAME, "ssn1")
    SSN2 = (By.NAME, "ssn2")
    SSN3 = (By.NAME, "ssn3")
    DATE_OF_BIRTH_MONTH = (By.NAME, "dateofbirthmonth")
    DATE_OF_BIRTH_DAY = (By.NAME, "dateofbirthday")
    DATE_OF_BIRTH_YEAR = (By.NAME, "dateofbirthyear")


class FinalPageLocators(object):
    USER_NAME = (By.NAME, "user_name")
    PASSWORD = (By.NAME, "password")
    VERIFY_PASSWORD = (By.NAME, "verify_password")
    SECRET_QUESTION = (By.NAME, "secret_question")
    SECRET_ANSWER = (By.NAME, "answer")
    CC_NAME_ON_CARD = (By.NAME, "cc_nameoncard")
    CC_NUMBER = (By.NAME, "cc_num")
    CC_EXPIRY_MONTH = (By.NAME, "cc_exp_month")
    CC_EXPIRY_YEAR = (By.NAME, "cc_exp_year")
    CC_CVV = (By.NAME, "cc_cvv")
    HOME_SAME_AS_BILLING_YES = (By.NAME, "input[name='homesameasbilling'][value='yes']")
    HOME_SAME_AS_BILLING_NO = (By.NAME, "input[name='homesameasbilling'][value='no']")