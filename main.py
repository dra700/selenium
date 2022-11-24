from selenium import webdriver

url = "https://spo.isdc.co.kr"

driver = webdriver.Chrome()
driver.get(url)
driver.quit()