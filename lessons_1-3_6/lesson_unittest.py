import unittest
import time
from selenium import webdriver


def webdriverChrome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(options=options)

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.browser = webdriverChrome()

    def tearDown(self):
        self.browser.quit()

    def registration(self, link):
        browser = self.browser
        browser.get(link)

        fields = {
            ".first_block .first": "Ivan",
            ".first_block .second": "Petrov",
            ".first_block .third": "ivan@gmail.com",
        }
        for selector, value in fields.items():
            browser.find_element_by_css_selector(selector).send_keys(value)

        browser.find_element_by_css_selector("button.btn").click()

        time.sleep(1)
        welcome_text = browser.find_element_by_tag_name("h1").text
        
        self.assertTrue("successfully" in welcome_text, "registration is failed")

    def test_registration1(self):
        self.registration("http://suninjuly.github.io/registration1.html")

    def test_registration2(self):
        self.registration("http://suninjuly.github.io/registration2.html")
    

if __name__ == "__main__":
    unittest.main()