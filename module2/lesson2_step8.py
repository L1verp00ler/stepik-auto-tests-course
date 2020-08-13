from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Имя")

    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Фамилия")

    email = browser.find_element_by_name("email")
    email.send_keys("test@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_file.txt')
    attach_file = browser.find_element_by_id("file")
    attach_file.send_keys(file_path)

    '''
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file
    '''

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
