from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By



options = webdriver.ChromeOptions()


driver = webdriver.Chrome(options=options)


driver.get("https://google.com")

time.sleep(5)

search=driver.find_element(By.CSS_SELECTOR,".gLFyf")
search.send_keys("Test Automation")
search.send_keys(Keys.RETURN)
time.sleep(10)

