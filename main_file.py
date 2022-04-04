from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser,15).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"100"))
    book = browser.find_element_by_id("book")
    book.click()
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    submit_button = browser.find_element_by_id("solve")
    submit_button.click()
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir,'test.txt')
    # first = browser.find_element_by_css_selector("[name='firstname']")
    # first.send_keys('Ivan')
    # last = browser.find_element_by_css_selector("[name='lastname']")
    # last.send_keys('Petrov')
    # email = browser.find_element_by_css_selector("[name='email']")
    # email.send_keys('test@test.com')
    #
    # file = browser.find_element_by_id('file')
    # file.send_keys(file_path)

    # button = browser.find_element_by_tag_name("button")
    # button.click()
    # new_window = browser.window_handles[1]
    # browser.switch_to_window(new_window)
    # x = browser.find_element_by_id("input_value").text
    # answer = browser.find_element_by_id("answer")
    # answer.send_keys(y)
    # submit_button = browser.find_element_by_class_name("btn.btn-primary")
    # submit_button.click()
    print(browser.switch_to_alert().text)

finally:
    # закрываем браузер после всех манипуляций
    # time.sleep(10)
    browser.quit()