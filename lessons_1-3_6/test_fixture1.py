from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

def webdriverChrome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(options=options)

class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriverChrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser = webdriverChrome()
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriverChrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")