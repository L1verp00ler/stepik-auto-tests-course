import pytest
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]

linkss = [
    'https://stepik.org/lesson/236895/step/1'
]


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_new_task(browser, link):
    #browser = webdriver.Chrome()

    browser.get(link)
    answer = math.log(int(time.time()))

    #button = WebDriverWait(browser, 5).until(
    #    EC._element_if_visible((By.ID, "verify"))
    #)
    #button.click()

    time.sleep(5)

    browser.find_element_by_tag_name("textarea").send_keys(str(answer))

    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    time.sleep(2)

    message = browser.find_element_by_class_name("smart-hints__hint")
    assert "Correct!" == message.text, "Некорректный ответ!"

    time.sleep(5)

    #browser.quit()
