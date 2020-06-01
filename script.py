"""
Install selenium by pip install selenium
also download the chroedriver from 'https://chromedriver.chromium.org/downloads' same as your chrome browser version
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

input('Enter Any Key To Continue >>> ')

option=Options()
option.add_argument('user-data-dir=selenium')

# Open Chrome Browser with help of ChromeDriver and Selenium
driver = webdriver.Chrome('Paste Your ChromeDriver path here' , options=option)
time.sleep(3)

def login(userName,passWord):

    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(4)

    #find Xpath og userName Field
    userField = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
    userField.clear()
    userField.send_keys(userName)
    time.sleep(4)

    # find Xpath of Password Field
    pwdField = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
    pwdField.clear()
    pwdField.send_keys(passWord+Keys.RETURN)
    time.sleep(4)


login('Username', 'Password') # Pass userName and Password here.
time.sleep(4)