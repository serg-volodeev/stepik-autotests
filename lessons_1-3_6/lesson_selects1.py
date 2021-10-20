from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 


def webdriverChrome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(options=options)

try:
    browser = webdriverChrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text

    result = str(int(num1) + int(num2))

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(result) # ищем элемент с текстом "Python"
    # print(result)
    
    browser.find_element_by_css_selector(".btn-default").click()
   

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла