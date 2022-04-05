import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def test_page1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(by=By.XPATH, value = "//form/div[contains(@class,'first_block')]//input[contains(@class, 'form-control first')]")
        input1.send_keys("Ivan")
        input2 =  browser.find_element(by=By.XPATH, value = "//form/div[contains(@class,'first_block')]//input[contains(@class, 'form-control second')]")
        input2.send_keys("Ivanov")
        input3 =  browser.find_element(by=By.XPATH, value = "//form/div[contains(@class,'first_block')]//input[contains(@class, 'form-control third')]")
        input3.send_keys("Ivan@ivan.ru")

        button = browser.find_element(by=By.CSS_SELECTOR, value = "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element(by=By.TAG_NAME, value = "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text,"Congratulations! You have successfully registered!")
        browser.quit()

    def test_page2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(by=By.XPATH, value = "//form/div[contains(@class,'first_block')]//input[contains(@class, 'form-control first')]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(by=By.XPATH, value = "//form/div[contains(@class,'first_block')]//input[contains(@class, 'form-control second')]")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(by=By.XPATH, value = "//form/div[contains(@class,'first_block')]//input[contains(@class, 'form-control third')]")
        input3.send_keys("Ivan@ivan.ru")

        button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")

        time.sleep(1)
        welcome_text_elt = browser.find_element(by=By.TAG_NAME, value = "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        browser.quit()

if __name__ == '__main__':
    unittest.main()
