import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class QaAutomationAssessmentOrig(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_pixel_fired(self):
        driver = self.driver
        driver.implicitly_wait(10)

        driver.get("https://www.gofreecredit.com/r/51196bc4ac/?subid=QAAssessment&prods=tu3&codes=success")

        assert "Free Credit Score and Triple Credit Scores" in driver.title

        assert "Do You Know Your Credit Score?" in driver.page_source

        fname = driver.find_element_by_name("fname")
        fname.send_keys("First")

        lname = driver.find_element_by_name("lname")
        lname.send_keys("Last")

        email = driver.find_element_by_name("email")
        email.send_keys("test@example.com")

        zip = driver.find_element_by_name("zip")
        zip.send_keys("90245")

        # click on submit button
        driver.find_element_by_xpath("//button[@type='submit']").click()

        assert "Start Here" in driver.page_source

        address1 = driver.find_element_by_name("address1")
        address1.send_keys("123 Main street")

        city = driver.find_element_by_name("city")
        city.clear()
        city.send_keys("El Segundo")

        state = Select(driver.find_element_by_name("state"))
        state.select_by_value("CA")

        driver.find_element_by_css_selector("input[name='lived_more_six_months'][value='yes']").click()

        phone1 = driver.find_element_by_name("phone1")
        phone1.click()
        phone1.send_keys("3102979233")

        ssn3 = driver.find_element_by_name("ssn3")
        ssn3.send_keys("0001")

        dateofbirthmonth = Select(driver.find_element_by_name("dateofbirthmonth"))
        dateofbirthmonth.select_by_value("02")

        dateofbirthday = Select(driver.find_element_by_name("dateofbirthday"))
        dateofbirthday.select_by_value("02")

        dateofbirthyear = Select(driver.find_element_by_name("dateofbirthyear"))
        dateofbirthyear.select_by_value("1990")

        # click on submit button
        driver.find_element_by_xpath("//button[@type='submit']").click()

        driver.find_element_by_id("errorContainer")

        assert "Your SSN could not be found based on your last 4 digits, please enter all 9 digits of your SSN" in driver.page_source

        driver.find_element_by_css_selector("a[class='ui-dialog-titlebar-close ui-corner-all']").click()

        ssn1 = driver.find_element_by_name("ssn1")
        ssn1.send_keys("000")

        ssn2 = driver.find_element_by_name("ssn2")
        ssn2.send_keys("00")

        # click on submit button
        driver.find_element_by_xpath("//button[@type='submit']").click()

        assert "In Order to Verify Your Identity, Please Answer the Following Security Questions:" in driver.page_source

        # click on submit button
        driver.find_element_by_xpath("//button[@type='submit']").click()

        user_name = driver.find_element_by_name("user_name")
        user_name.clear()
        user_name.send_keys("qa@example.com")

        password = driver.find_element_by_name("password")
        password.send_keys("Password12")

        verify_password = driver.find_element_by_name("verify_password")
        verify_password.send_keys("Password12")

        secret_question = Select(driver.find_element_by_name("secret_question"))
        secret_question.select_by_value("What city were you born in?")

        secret_answer = driver.find_element_by_name("secret_answer")
        secret_answer.send_keys("Manila")

        cc_nameoncard = driver.find_element_by_name("cc_nameoncard")
        cc_nameoncard.send_keys("First Last")

        cc_num = driver.find_element_by_name("cc_num")
        cc_num.send_keys("4111111111111111")

        cc_exp_month = Select(driver.find_element_by_name("cc_exp_month"))
        cc_exp_month.select_by_value("01")

        cc_exp_year = Select(driver.find_element_by_name("cc_exp_year"))
        cc_exp_year.select_by_value("2016")

        cc_cvv = driver.find_element_by_name("cc_cvv")
        cc_cvv.send_keys("123")

        driver.find_element_by_css_selector("input[name='homesameasbilling'][value='yes']").click()

        # click on submit button
        driver.find_element_by_xpath("//button[@type='submit']").click()

        alert = driver.switch_to.alert

        assert "Pixel Fired: QAAssessment" in alert.text

        alert.accept

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()