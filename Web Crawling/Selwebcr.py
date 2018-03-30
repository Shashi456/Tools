from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

#“”” Save a screenshot from spotify.com in current directory. “””
#DRIVER = webdriver.Chrome('G://Code//Tools for fun//chromedriver.exe')
options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size=1200x800')



driver = webdriver.Chrome('G://Code//Tools for fun//chromedriver.exe',chrome_options=options) R
driver.get('') # Put the site name
#print(driver.get_cookies())


#The following lines are for logging in, we can't automate crawling with captcha logins.
#username = driver.find_element_by_name("username")
#password = driver.find_element_by_name("password")
#username.send_keys("pawss") # put username
#password.send_keys("As")  # put password
#driver.delete_all_cookies()loader
#driver.find_element_by_class_name("submit").click()

cookies =[
{ }
]

#adding multiple cookies to driver
#A couple of things to keep in mind: 
# 1. Add cookie in selenium format , minimum req : {'name':'', 'value': ''}
# 2. If adding cookie to a driver, first get the website and then add cookies
for cookie in cookies:
    driver.add_cookie(cookie)

#print(driver.get_cookie())

driver.get('')#after getting cookie
driver.implicitly_wait(900) # different ways of stopping the browser so that the website can load
WebDriverWait(driver,200)
time.sleep(20)
screenshot = driver.save_screenshot('my_screenshot.png') #take screenshot
driver.quit()
