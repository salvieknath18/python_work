# import Selenium
from selenium import webdriver

# Webdriver Configuration with chrome driver
driver = webdriver.Chrome(r"D:\selenium\drivers\chromedriver.exe")
# Maximize browser window
driver.maximize_window()
# Load Web APP/URL
driver.set_page_load_timeout("50")
driver.get(r"https://naukri.com")  # this website opens with multiple window popups
Allwindow = driver.window_handles
mainwindow = None
for win in Allwindow:
    driver.switch_to.window(win)
    print(driver.current_url)
    if driver.current_url == "https://naukri.com":
        print("This is my main window")
        mainwindow = win
    else:
        driver.close()
driver.switch_to.window(mainwindow)
print(driver.current_url)

driver.get(r"https://thetestingworld.com/testings/")
driver.find_element_by_xpath("//label[text()='Login]").click()
driver.find_element_by_name("_txtUserName").send_keys("test")
driver.find_element_by_name("_txtPassword").send_keys("test")
driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
driver.find_element_by_xpath("//a[contains(text(), 'My Account')]").click()
driver.find_element_by_xpath("//a[contains(text(), 'Delete')]").click()

Alltabs = driver.window_handles
print(Alltabs)
main_tab = None
for tab in Alltabs:
    driver.switch_to.window(tab)
    print(driver.current_url)
    if driver.current_url == r"https://thetestingworld.com/testings/manage_customer.php":
        # here for comparison if url is dynamic then we can use title or any other element
        driver.find_element_by_xpath("//button[text()='start download']").click()
        print("This is my main window")
        main_tab = tab
    else:
        driver.close()
driver.switch_to.window(main_tab)
print(driver.current_url)

driver.get("https://toolsqa.com/iframe-practice-page/")