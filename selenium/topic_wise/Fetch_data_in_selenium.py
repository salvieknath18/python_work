# import Selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
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

print(driver.title)
print(driver.current_url)
print("*****************************************************************")
# get page source
print(driver.page_source)

print("*****************************************************************")
# Fetch element text
print(driver.find_element_by_class_name("displayPopup").text)

# Fetching attribute value of an element
driver.find_element_by_xpath("//input[@type='submit]").get_attribute("value")

sel_obj = Select(driver.find_element_by_name("sex"))
sel_obj.select_by_visible_text("Male")
# Fetch selected object
print(sel_obj.first_selected_option.text)
print(sel_obj.all_selected_options)
print(sel_obj.options)
for op in sel_obj.options:
    print(op.text)

