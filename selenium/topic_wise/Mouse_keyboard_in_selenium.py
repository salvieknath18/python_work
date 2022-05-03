# import Selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Webdriver Configuration with chrome driver
driver = webdriver.Chrome(r"D:\selenium\drivers\chromedriver.exe")


# Load Web APP/URL
driver.set_page_load_timeout("50")
driver.get(r"https://thetestingworld.com/testings/")

# Maximize browser window
driver.maximize_window()

driver.find_element_by_name('fld_username').send_keys("ABCD")
action = ActionChains(driver)
action.send_keys(Keys.CONTROL).send_keys('a').perform()
time.sleep(5)

time.sleep(5)

action.send_keys(Keys.ESCAPE).perform()
time.sleep(5)
action.context_click()
time.sleep(5)
action.click(driver.find_element_by_id("tab2"))
time.sleep(10)

driver.close()