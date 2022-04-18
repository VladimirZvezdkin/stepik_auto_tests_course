import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestPage():
    links = ["https://stepik.org/lesson/236895/step/1",
             "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1",
             "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1",
             "https://stepik.org/lesson/236905/step/1"]

    @pytest.mark.parametrize('link',links)
    def test_page(self,browser,link):
        link = f"{link}"
        browser.get(link)
        wait = WebDriverWait(browser,10)
        textarea = wait.until(EC.visibility_of_element_located((By.TAG_NAME,"textarea")))
        answer = math.log(int(time.time()))
        textarea.send_keys(str(answer))
        button_submit = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        button_submit.click()
        message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        message_text = message.text

        assert message_text == 'Correct!', 'Test failed! Not correct!'








