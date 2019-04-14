from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import re  
import random
import string
import time
import os

website_link="https://decoy-captive.000webhostapp.com/portal.html"
def randomstring(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')


username = randomstring()

password=randomstring()

email=randomstring() +"@gmail.com"

element_for_username="auth_user"
element_for_email="auth_email"
element_for_password="auth_pass"
element_for_checkbox="checkbox"
element_for_submit="login"



browser = webdriver.Chrome(chrome_options=options)
browser.get((website_link))    

browser.find_element_by_id("auth_email").send_keys(email)
browser.find_element_by_id("auth_user").send_keys(username)
browser.find_element_by_id("auth_pass").send_keys(password)
browser.find_element_by_id("checkbox").click()
browser.find_element_by_id("login").click()
browser.save_screenshot('screen.png')


delay = 5 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'error')))
    print("Legitimate captive portal!")

except TimeoutException:
    print("Phishing captive portal!")


# if browser.find_element_by_id("error"):
#     print("Nothing to worry about! This wireless network is secured.")

# elif True:
#     print("Phishing captive portal!")
