import unittest
from page import FinalPage
from page import PageOne
from page import PageTwo
from page import PixelPage
from page import VerifyIdentityPage
from selenium import webdriver

class PixelFiredTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.gofreecredit.com/r/51196bc4ac/?subid=QAAssessment&prods=tu3&codes=success")

# TESTS

    def test_pixel_fired(self):
        self.fill_out_page_one()
        self.fill_out_page_two()
        self.fix_full_ssn()
        self.submit_verify_identity_page()
        self.fill_out_final_page()
        self.verify_pixel_fired()

# HELPER FUNCTIONS

    def fill_out_page_one(self):
        page_one = PageOne(self.driver)

        assert page_one.is_title_matches(), "Title does not match."
        assert page_one.is_page_text_present(), "Page text is not present."

        page_one.first_name = "First"
        page_one.last_name = "Last"
        page_one.email = "test@example.com"
        page_one.zip = "90245"

        page_one.click_submit_button()

    def fill_out_page_two(self):
        page_two = PageTwo(self.driver)

        assert page_two.is_page_text_present(), "Page text is not present."

        page_two.address1 = "123 Main street"
        page_two.city = "El Segundo"
        page_two.state = "CA"
        page_two.lived_more_six_months = "yes"
        page_two.phone1 = "3102979233"
        page_two.ssn3 = "0001"
        page_two.date_of_birth_month = "02"
        page_two.date_of_birth_day = "02"
        page_two.date_of_birth_year = "1990"

        page_two.click_submit_button()

    def fix_full_ssn(self):
        page_two = PageTwo(self.driver)

        assert page_two.is_error_present("Your SSN could not be found based on your last 4 digits, please enter all 9 digits of your SSN"), "Error is not present."

        page_two.close_error_dialog()

        page_two.ssn1 = "000"
        page_two.ssn2 = "00"

        page_two.click_submit_button()

    def submit_verify_identity_page(self):
        verify_identity_page = VerifyIdentityPage(self.driver)

        assert verify_identity_page.is_page_text_present(), "Page text is not present."

        verify_identity_page.click_submit_button()

    def fill_out_final_page(self):
        final_page = FinalPage(self.driver)

        final_page.user_name = "qa@example.com"
        final_page.password = "Password12"
        final_page.verify_password = "Password12"
        final_page.secret_question = "What city were you born in?"
        final_page.secret_answer = "Manila"
        final_page.cc_name_on_card = "First Last"
        final_page.cc_number = "4111111111111111"
        final_page.cc_expiry_month = "01"
        final_page.cc_expiry_year = "2016"
        final_page.cc_cvv = "123"
        final_page.home_same_as_billing = "yes"

        final_page.click_submit_button()

    def verify_pixel_fired(self):
        pixel_page = PixelPage(self.driver)

        assert pixel_page.is_pixel_fired(), "Pixel is not fired."

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()