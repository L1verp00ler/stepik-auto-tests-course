from selenium import webdriver

link = 'http://suninjuly.github.io/registration2.html' # Укажите ссылку

FirstName = 'Ivan'
LastName = 'Ivanov'
Email = 'ivanov@mail.ru'
Phone = '81234567890'
Address = 'Tomsk'

browser = webdriver.Chrome()
browser.get(link)
firstName = browser.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys(FirstName)
lastName = browser.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys(LastName)
email = browser.find_element_by_css_selector('[placeholder="Input your email"]').send_keys(Email)
phone = browser.find_element_by_css_selector('[placeholder="Input your phone:"]').send_keys(Phone)
address = browser.find_element_by_css_selector('[placeholder="Input your address:"]').send_keys(Address)
button = browser.find_element_by_tag_name('button').click()


