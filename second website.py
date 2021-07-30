from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests
import time
import random
import sys
from webdriver_manager.chrome import ChromeDriverManager


print("Enter phone number")
phone_number = int(input())
print("Enter number of messages to be sent")
numtime = int(input())
options = Options()
options.add_argument('--headless')
options.add_argument("--incognito")
options.add_argument('--disable-gpu')
wd = webdriver.Chrome("/Users/anchitshrivastava/.wdm/drivers/chromedriver/mac64/92.0.4515.43/chromedriver",options = options)

wd.get("https://www.flipkart.com/")
time.sleep(random.uniform(2.1,3.2))
print("browser opened")

try:
	login_button = wd.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[3]/div/div/div/a').click()
except:
	print("no need")
time.sleep(random.uniform(2.1,3.2))

print("login button clicked")

input_box = wd.find_element_by_css_selector("input._2IX_2-.VJZDxU")
input_box.click()
time.sleep(random.uniform(2.1,3.2))

print("input located")
try:
	input_box.clear()
	input_box.send_keys(phone_number)
	time.sleep(random.uniform(2.1,3.2))
except:
	wd.close()
	sys.exit()

send_otp = wd.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[5]/button').click()
print("1 otp sent")
time.sleep(random.uniform(15.1,21.2))

for i in range(numtime):
	wd.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/div/div[3]/span').click()
	print(i+2,end = " ")
	print("otp sent")
	time.sleep(random.uniform(2.1,3.2))




