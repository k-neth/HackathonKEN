from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

import random


options = webdriver.ChromeOptions()


driver = webdriver.Chrome(options=options)

driver.get("https://www.facebook.com/login")

time.sleep(5)


try:
        
    username=driver.find_element(By.ID,"email")
    username.send_keys('username')
  
    mypassword = driver.find_element(By.ID, "pass")
    mypassword.send_keys("password")
    mypassword.send_keys(Keys.RETURN)

    time.sleep(5)


except:
    pass










