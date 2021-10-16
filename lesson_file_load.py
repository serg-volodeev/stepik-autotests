from selenium import webdriver
import time
import os

def webdriverChrome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(options=options)

try:
    browser = webdriverChrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    data = {"firstname": "Ivan", "lastname": "Petrov", "email": "ivan@gmail.com"}

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')

    for name, value in data.items():
        browser.find_element_by_name(name).send_keys(value)

    browser.find_element_by_id("file").send_keys(file_path)

    browser.find_element_by_css_selector(".btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла