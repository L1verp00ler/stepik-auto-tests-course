from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
#import pyperclip

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажать на кнопку "Забронировать"
    browser.find_element_by_id("book").click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)

    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    '''
    # Копирование числа из алерта в буфер обмена
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    '''
    time.sleep(10)
    browser.quit()
