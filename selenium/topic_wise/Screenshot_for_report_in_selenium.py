# import Selenium
from selenium import webdriver

# Webdriver Configuration with chrome driver
driver = webdriver.Chrome(r"D:\selenium\drivers\chromedriver.exe")

# Load Web APP/URL
driver.set_page_load_timeout("50")
driver.get(r"https://thetestingworld.com/testings/")

# Maximize browser window
driver.maximize_window()
driver.g
driver.get_screenshot_as_file(r"D:\selenium\img1.png")
# or we can define a function for screenshot for dynamic name of file

