import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.maximize_window()

driver.get('https://www.amazon.com/')

# go to register page
driver.find_element_by_link_text('Start here.').click()
# driver.find_element_by_id('nav-flyout-ya-newCust').click()

# fill information
driver.find_element_by_id('ap_customer_name').send_keys('Saphire')
driver.find_element_by_id('ap_email').send_keys('+6287886177686')
driver.find_element_by_id('ap_password').send_keys('')
driver.find_element_by_id('ap_password_check').send_keys('')
driver.find_element_by_id('continue').click()

# fill the captcha or otp
time.sleep(120)
