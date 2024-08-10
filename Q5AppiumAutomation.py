from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


desired_caps = {
    "platformName": "Android",           
    "platformVersion": "10",              
    "deviceName": "emulator-5554",        
    "app": "/path/to/your/app.apk",       
    "automationName": "UiAutomator2"      
}


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

try:
   
    wait = WebDriverWait(driver, 10)
    
 
    username_field = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example:id/username")))
    password_field = driver.find_element(AppiumBy.ID, "com.example:id/password")
    login_button = driver.find_element(AppiumBy.ID, "com.example:id/login")

    username_field.send_keys("your_username")
    password_field.send_keys("your_password")
    login_button.click()


    settings_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example:id/settings")))
    settings_button.click()

 
    profile_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example:id/profile")))
    profile_button.click()

  
    display_name_field = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example:id/displayName")))
    save_button = driver.find_element(AppiumBy.ID, "com.example:id/save")

    display_name_field.clear()
    display_name_field.send_keys("New Display Name")
    save_button.click()

    
    updated_display_name = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example:id/displayName")))
    assert updated_display_name.text == "New Display Name", "Profile update failed"

    print("Test passed: Profile updated successfully.")

finally:
    
    driver.quit()
