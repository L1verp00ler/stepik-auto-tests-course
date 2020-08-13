import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/138920/step/2?unit=196194"

try:
    driver = webdriver.Chrome()
    time.sleep(5)

    driver.get(link)
    time.sleep(5)

    button = driver.find_element(By.ID, "ember62")
finally:
    driver.quit()
