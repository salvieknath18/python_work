from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(r"D:\selenium\drivers\chromedriver.exe")

driver.set_page_load_timeout("10")
driver.get(r"https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.maximize_window()

driver.find_element_by_id("user-message").send_keys("this is test message")
time.sleep(5)
#buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Show Message')]")
button = driver.find_elements_by_xpath("//button[contains(text(), 'Show Message')]")[0]
button.click()
time.sleep(5)

driver.find_element_by_id("sum1").send_keys(30)
driver.find_element_by_id("sum2").send_keys(20)
time.sleep(2)
button = driver.find_elements_by_xpath("//button[contains(text(), 'Get Total')]")[0]
button.click()
time.sleep(3)
driver.find_element_by_id("sum1").clear()
driver.find_element_by_id("sum2").clear()

driver.find_element_by_id("sum1").send_keys('AB')
driver.find_element_by_id("sum2").send_keys(20)
time.sleep(2)
button = driver.find_elements_by_xpath("//button[contains(text(), 'Get Total')]")[0]
button.click()
time.sleep(3)
driver.find_element_by_id("sum1").clear()
driver.find_element_by_id("sum2").clear()

driver.find_element_by_id("sum1").send_keys(30)
driver.find_element_by_id("sum2").send_keys('ab')
time.sleep(2)
button = driver.find_elements_by_xpath("//button[contains(text(), 'Get Total')]")[0]
button.click()
time.sleep(3)
driver.find_element_by_id("sum1").clear()
driver.find_element_by_id("sum2").clear()

driver.find_element_by_id("sum1").send_keys('%$')
driver.find_element_by_id("sum2").send_keys('#$')
time.sleep(2)
button = driver.find_elements_by_xpath("//button[contains(text(), 'Get Total')]")[0]
button.click()
time.sleep(3)
driver.find_element_by_id("sum1").clear()
driver.find_element_by_id("sum2").clear()
#btn = driver.find_element_by_name("btnK").click()


#ActionChains(webdriver).move_to_element(btn).click(btn)


#driver.refresh()
driver.close()
