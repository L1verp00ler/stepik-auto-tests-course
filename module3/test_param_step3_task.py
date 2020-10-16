import pytest
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_new_task(browser, link):
    answer = math.log(int(time.time()))
    browser.get(link)

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'textarea'))
    ).send_keys(str(answer))

    browser.find_element_by_class_name("submit-submission").click()

    message = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
    )

    assert "Correct!" == message.text, "Некорректный ответ!"

    time.sleep(2)
