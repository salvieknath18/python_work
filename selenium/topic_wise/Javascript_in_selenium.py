# import Selenium
from selenium import webdriver

# Webdriver Configuration with chrome driver
driver = webdriver.Chrome(r"D:\selenium\drivers\chromedriver.exe")

# Load Web APP/URL
driver.set_page_load_timeout("50")
driver.get(r"https://thetestingworld.com/testings/")

# Maximize browser window
driver.maximize_window()

driver.execute_script("window.scrollTo(0, 400);")
# selenium can only automate the task on web page not on browser
# so to execute the activity like scroll down must be done through javascript


