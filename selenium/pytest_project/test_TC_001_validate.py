# import Selenium
from selenium import webdriver
import pytest
from selenium.webdriver.support.select import Select

def test_validate_username():
    # Webdriver Configuration with chrome driver
    driver = webdriver.Chrome(r"D:\selenium\drivers\chromedriver.exe")

    # Load Web APP/URL
    driver.set_page_load_timeout("50")
    driver.get(r"https://thetestingworld.com/testings/")

    # Maximize browser window
    driver.maximize_window()
    values = ['abc', 'abcd', 'ab', 'abcde', '123123', '32434']
    for val in values:
        driver.find_element_by_name("username").send_keys(val)
        
    print(driver.title)
