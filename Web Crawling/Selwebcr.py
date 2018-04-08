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

# the following lines are for interacting with a table
# now something to keep in mind is the xpath will always work
# the only mistake you can do is xpath is defined differently for firefox and chrome 
# so when trying to interact with an element use the xpath according the WebDriver you are using 
#x1 = driver.find_element_by_xpath('//*[@id="bottom-area"]/div[2]/div[2]/div/div/div/div/table/tbody[6]/tr[1]/td[5]')
#x2 = driver.find_element_by_xpath('//*[@id="bottom-area"]/div[2]/div[2]/div')
#time.sleep(5)

#driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', x2)
#x1 = x.get_attribute("innerHTML")
#x2 = x.get_attribute("value")
#print(x1)

#print(driver.get_cookie())

driver.get('')#after getting cookie
driver.implicitly_wait(900) # different ways of stopping the browser so that the website can load
WebDriverWait(driver,200)
time.sleep(20)
screenshot = driver.save_screenshot('my_screenshot.png') #take screenshot
driver.quit()
