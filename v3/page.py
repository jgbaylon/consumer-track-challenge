from element import Address1Element
from element import CcCvvElement
from element import CcExpiryMonthElement
from element import CcExpiryYearElement
from element import CcNameOnCardElement
from element import CcNumberElement
from element import CityElement
from element import DateOfBirthDayElement
from element import DateOfBirthMonthElement
from element import DateOfBirthYearElement
from element import EmailElement
from element import FirstNameElement
from element import HomeSameAsBillingYesElement
from element import LastNameElement
from element import LivedMoreSixMonthsYesElement
from element import PasswordElement
from element import Phone1Element
from element import SecretAnswerElement
from element import SecretQuestionElement
from element import Ssn1Element
from element import Ssn2Element
from element import Ssn3Element
from element import StateElement
from element import SubmitButtonElement
from element import UserNameElement
from element import VerifyPasswordElement
from element import ZipElement

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class FormPage(BasePage):

    def click_submit_button(self):
        submit_button = SubmitButtonElement(self.driver)
        submit_button.click()

    def is_text_in_title(self, text):
        return text in self.driver.title

    def is_text_in_page_source(self, text):
        return text in self.driver.page_source

    def is_error_present(self, error_message):
        try:
            self.driver.find_element_by_id("errorContainer")
            return error_message in self.driver.page_source
        except:
            return False

    def close_error_dialog(self):
        self.driver.find_element_by_css_selector("a[class='ui-dialog-titlebar-close ui-corner-all']").click()


class PageOne(FormPage):

    first_name = FirstNameElement()
    last_name = LastNameElement()
    email = EmailElement()
    zip = ZipElement()

    def is_title_matches(self):
        return self.is_text_in_title("Free Credit Score and Triple Credit Scores")

    def is_page_text_present(self):
        return self.is_text_in_page_source("Do You Know Your Credit Score?")


class PageTwo(FormPage):

    address1 = Address1Element()
    city = CityElement()
    state = StateElement()
    lived_more_six_months = LivedMoreSixMonthsYesElement()
    phone1 = Phone1Element()
    ssn1 = Ssn1Element()
    ssn2 = Ssn2Element()
    ssn3 = Ssn3Element()
    date_of_birth_month = DateOfBirthMonthElement()
    date_of_birth_day = DateOfBirthDayElement()
    date_of_birth_year = DateOfBirthYearElement()

    def is_page_text_present(self):
        return self.is_text_in_page_source("Start Here")


class VerifyIdentityPage(FormPage):

    def is_page_text_present(self):
        return self.is_text_in_page_source("In Order to Verify Your Identity, Please Answer the Following Security Questions:")


class FinalPage(FormPage):

    user_name = UserNameElement()
    password = PasswordElement()
    verify_password = VerifyPasswordElement()
    secret_question = SecretQuestionElement()
    secret_answer = SecretAnswerElement()
    cc_nameoncard = CcNameOnCardElement()
    cc_num = CcNumberElement()
    cc_exp_month = CcExpiryMonthElement()
    cc_exp_year = CcExpiryYearElement()
    cc_cvv = CcCvvElement()
    home_same_as_billing = HomeSameAsBillingYesElement()


class PixelPage(BasePage):

    def is_pixel_fired(self):
        alert = self.driver.switch_to.alert
        return "Pixel Fired: QAAssessment" in alert.text