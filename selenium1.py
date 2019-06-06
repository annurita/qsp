from selenium import webdriver
driver =webdriver.Chrome(executable_path="C:/Users/Anurita Kumari/Downloads/chromedriver.exe")
driver.get("http://www.facebook.com")
driver.implicitly_wait(30)
driver.find_element_by_name("firstname").send_keys("Annuu")
driver.find_element_by_name("lastname").send_keys("singh")
driver.find_element_by_xpath('//input[contains("@aria-label number")]').send_keys("7903679373")

