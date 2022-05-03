from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome(r"D:\selenium\drivers\chromedriver.exe")

driver.set_page_load_timeout("10")
driver.get(r"https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.maximize_window()

driver.find_element_by_id("user-message").send_keys("this is test message")
#time.sleep(5)
#buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Show Message')]")
button = driver.find_elements_by_xpath("//button[contains(text(), 'Show Message')]")[0]
button.click()
driver.find_element_by_id("display")


#time.sleep(5)

sum1 = [30, 'ab', 30, '$%', '30A', 'dfg30']
sum2 = [20, 20, 'ab', '$#', '20fgg', 'fgfg20']

for i in range(len(sum1)):
    driver.find_element_by_id("sum1").send_keys(sum1[i])
    #time.sleep(1)
    driver.find_element_by_id("sum2").send_keys(sum2[i])
    #time.sleep(1)
    button = driver.find_elements_by_xpath("//button[contains(text(), 'Get Total')]")[0]
    button.click()
    #time.sleep(2)
    driver.find_element_by_id("sum1").clear()
    driver.find_element_by_id("sum2").clear()

driver.close()
