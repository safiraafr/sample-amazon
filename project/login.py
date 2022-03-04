from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element_by_xpath('//*[@id="nav-signin-tooltip"]/a').click()
driver.find_element_by_id('ap_email').send_keys('+6287886177686')
driver.find_element_by_id('continue').click()
driver.find_element_by_id('ap_password').send_keys('****')
driver.find_element_by_id('signInSubmit').click()
