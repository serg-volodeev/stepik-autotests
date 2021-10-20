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
    # browser.execute_script("document.title='Script executing';alert('Robots at work');")
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)


    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()

    rule = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rule)
    rule.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()   

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла