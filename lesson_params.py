import time
import math
import pytest
from selenium import webdriver

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]

@pytest.fixture(scope="function")
def browser():
    # Убираем сообщения об ошибках при запуске Chrome
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.mark.parametrize('link', links)
def test_answer(browser, link):
    browser.get(link)
    browser.implicitly_wait(10)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_css_selector(".ember-text-area").send_keys(answer)
    browser.find_element_by_css_selector(".submit-submission").click()
    expected = "Correct!"
    got = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert got == expected, f"expected '{expected}', got '{got}'"


    