from selenium import webdriver
import time
import random
import string

letters = string.ascii_letters

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        word = ''.join(random.choice(letters) for _ in range(8))
        element.send_keys(word)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла