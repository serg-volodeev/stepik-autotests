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
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    browser.find_element_by_tag_name("button").click()
    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_tag_name("button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
