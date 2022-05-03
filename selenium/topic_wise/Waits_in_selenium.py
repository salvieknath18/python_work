# import Selenium
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Webdriver Configuration with chrome driver
driver = webdriver.Chrome(r"D:\selenium\drivers\chromedriver.exe")

# Load Web APP/URL
driver.set_page_load_timeout("50")
driver.get(r"https://thetestingworld.com/testings/")

# Maximize browser window
driver.maximize_window()

print(driver.title)

# Wait for 20 ses (***********forced wait*********)
# any statement after this wait has to wait for 20 sec anyway any how
time.sleep(20)

# Wait for 20 ses (**********implicitely wait**********)
# any element which we are finding wait for 20 sec before finding else give error
# if any element not exist it will give error immidiately or wait fro 20 for finding
driver.implicitly_wait(20) # generally used to check existance of the element

# Wait for 20 sec (**********Explicitely wait**********)
# this wait work on the property of the element
# eg. Enable or not, clickable or not, text present in element or not
# when we have to wait for property of the element to be change or specific condition to be perform
wait = WebDriverWait(driver, 20)
sel_obj = Select(driver.find_element_by_name("country"))
wait.until(ec.text_to_be_present_in_element((By.ID, "countryId"), "India"))
sel_obj.select_by_visible_text("India")

wait.until(ec.text_to_be_present_in_element((By.ID, "stateId"), "Delhi"))
sel_obj = Select(driver.find_element_by_id("stateId"))
sel_obj.select_by_visible_text("Delhi")
# muliple options are there with explicit wait check using wait.until(ec.)
