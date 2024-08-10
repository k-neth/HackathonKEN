from selenium import webdriver

def init_driver():
    driver = webdriver.Chrome()  # or use another browser
    driver.maximize_window()
    return driver

def quit_driver(driver):
    driver.quit()
