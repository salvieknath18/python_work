# import Selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Webdriver Configuration with chrome driver
driver = webdriver.Chrome(r"D:\selenium\drivers\chromedriver.exe")

# Load Web APP/URL
driver.set_page_load_timeout("10")
driver.get(r"https://www.google.com/")

# Maximize browser window
driver.maximize_window()

driver.find_element_by_name("q").send_keys("python")
time.sleep(10)

driver.find_element_by_name("btnK").click()
time.sleep(10)

driver.find_element_by_xpath("//div[@class='srg']/div[3]/div/div/div/a").click()
time.sleep(10)

driver.close()
