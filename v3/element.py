from locators import PageOneLocators
from locators import PageTwoLocators
from locators import FinalPageLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

class InputTextElement(object):

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)

        if self.should_focus:
            element.click()

        if self.should_clear:
            element.clear()
        
        element.send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")


class SelectElement(object):

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        element = Select(driver.find_element(*self.locator))

        if self.should_clear:
            element.deselect_all()
        
        element.select_by_value(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        element = Select(driver.find_element(*self.locator))
        return element.all_selected_options


class RadioButtonElement(object):

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))

        if self.should_clear:
            element.clear()

        if value in self.locator[1]:
            element = driver.find_element(*self.locator)
            element.click()

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")


class SubmitButtonElement(object):

    def __init__(self, driver):
        self.driver = driver

    def click(self):
        self.driver.find_element_by_xpath("//button[@type='submit']").click()


class FirstNameElement(InputTextElement):

    locator = PageOneLocators.FIRST_NAME
    should_focus = False
    should_clear = False


class LastNameElement(InputTextElement):

    locator = PageOneLocators.LAST_NAME
    should_focus = False
    should_clear = False


class EmailElement(InputTextElement):

    locator = PageOneLocators.EMAIL
    should_focus = False
    should_clear = False


class ZipElement(InputTextElement):

    locator = PageOneLocators.ZIP
    should_focus = False
    should_clear = False


class Address1Element(InputTextElement):

    locator = PageTwoLocators.ADDRESS1
    should_focus = False
    should_clear = False


class CityElement(InputTextElement):

    locator = PageTwoLocators.CITY
    should_focus = False
    should_clear = True


class StateElement(SelectElement):

    locator = PageTwoLocators.STATE
    should_clear = False


class LivedMoreSixMonthsYesElement(RadioButtonElement):

    locator = PageTwoLocators.LIVED_MORE_SIX_MONTHS_YES
    should_clear = False


class LivedMoreSixMonthsNoElement(RadioButtonElement):

    locator = PageTwoLocators.LIVED_MORE_SIX_MONTHS_NO
    should_clear = False


class Phone1Element(InputTextElement):

    locator = PageTwoLocators.PHONE1
    should_focus = False
    should_clear = False


class Phone1Element(InputTextElement):

    locator = PageTwoLocators.PHONE1
    should_focus = True
    should_clear = False


class Ssn1Element(InputTextElement):

    locator = PageTwoLocators.SSN1
    should_focus = False
    should_clear = False


class Ssn2Element(InputTextElement):

    locator = PageTwoLocators.SSN2
    should_focus = False
    should_clear = False


class Ssn3Element(InputTextElement):

    locator = PageTwoLocators.SSN3
    should_focus = False
    should_clear = False


class DateOfBirthMonthElement(SelectElement):

    locator = PageTwoLocators.DATE_OF_BIRTH_MONTH
    should_clear = False


class DateOfBirthDayElement(SelectElement):

    locator = PageTwoLocators.DATE_OF_BIRTH_DAY
    should_clear = False


class DateOfBirthYearElement(SelectElement):

    locator = PageTwoLocators.DATE_OF_BIRTH_YEAR
    should_clear = False


class UserNameElement(InputTextElement):

    locator = FinalPageLocators.USER_NAME
    should_focus = False
    should_clear = True


class PasswordElement(InputTextElement):

    locator = FinalPageLocators.PASSWORD
    should_focus = False
    should_clear = False


class VerifyPasswordElement(InputTextElement):

    locator = FinalPageLocators.VERIFY_PASSWORD
    should_focus = False
    should_clear = False


class SecretQuestionElement(SelectElement):

    locator = FinalPageLocators.SECRET_QUESTION
    should_clear = False


class SecretAnswerElement(InputTextElement):

    locator = FinalPageLocators.SECRET_ANSWER
    should_focus = False
    should_clear = False


class CcNameOnCardElement(InputTextElement):

    locator = FinalPageLocators.CC_NAME_ON_CARD
    should_focus = False
    should_clear = False


class CcNumberElement(InputTextElement):

    locator = FinalPageLocators.CC_NUMBER
    should_focus = False
    should_clear = False


class CcExpiryMonthElement(SelectElement):

    locator = FinalPageLocators.CC_EXPIRY_MONTH
    should_clear = False


class CcExpiryYearElement(SelectElement):

    locator = FinalPageLocators.CC_EXPIRY_YEAR
    should_clear = False


class CcCvvElement(InputTextElement):

    locator = FinalPageLocators.CC_CVV
    should_focus = False
    should_clear = False


class HomeSameAsBillingYesElement(RadioButtonElement):

    locator = FinalPageLocators.HOME_SAME_AS_BILLING_YES
    should_clear = False


class HomeSameAsBillingNoElement(RadioButtonElement):

    locator = FinalPageLocators.HOME_SAME_AS_BILLING_NO
    should_clear = False