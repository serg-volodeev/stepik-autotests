from selenium import webdriver
import time 
import math


def webdriverChrome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(options=options)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriverChrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    img = browser.find_element_by_id("treasure")
    x = img.get_attribute("valuex")
    y = calc(x)
    
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    browser.find_element_by_css_selector(".btn-default").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла