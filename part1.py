import time
import os
import subprocess
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

def start_appium_server():
    try:
        appium_executable = 'appium'
        appium_process = subprocess.Popen(appium_executable, shell=True)
        print("Appium server is starting...")
        
        time.sleep(10)  # Adjust the delay time as needed
        return appium_process
    except Exception as e:
        print(f"Error occurred while starting the Appium server: {e}")
        raise


def stop_appium_server(appium_server):
    try:
        appium_server.kill()
        print("Appium server is stopped.")
    except Exception as e:
        print(f"Error occurred while stopping the Appium server: {e}")
        raise
    

def quit_appium_session(driver):
    try:
        driver.quit()
    except Exception as e:
        print(f"Error occurred while quitting the Appium session: {e}")
        raise


desired_capabilities = {
    'platformName': 'ANDROID',
    'platformVersion': '29',  # Replace with the Android version of your device, e.g., '11.0'
    'deviceName': 'Samsung Galaxy S9',  # Replace with the name of your Android device
    'automationName': 'UiAutomator2',
    'udid': '4e42543832573398'  # Replace with the UDID of your Android device
}


appium_server_url = 'http://localhost:4723/wd/hub'
appium_server = start_appium_server()

driver = webdriver.Remote(appium_server_url, desired_capabilities)

app_package = 'app.simone'  # Replace with the package name of your app
driver.activate_app(app_package)
time.sleep(10)

xpath_to_click = "//android.widget.Button[@text='Not now']"
element = driver.find_element(MobileBy.XPATH, xpath_to_click)
element.click()
time.sleep(1)

xpath_to_click = "//android.widget.TextView[@text='arcade']"
element = driver.find_element(MobileBy.XPATH, xpath_to_click)
element.click()
time.sleep(1)

xpath_to_click = "//android.widget.TextView[@text='classic']"
element = driver.find_element(MobileBy.XPATH, xpath_to_click)
element.click()
time.sleep(1)

# Calculate the middle point of the screen
screen_width = driver.get_window_size()['width']
screen_height = driver.get_window_size()['height']
middle_x = screen_width // 2
middle_y = screen_height // 2
print("Middle coordinates:", middle_x, middle_y)

# Create a TouchAction instance and perform the tap action at the middle of the screen
tap_action = TouchAction(driver)
tap_action.tap(x=middle_x, y=middle_y).perform()


quit_appium_session(driver)
stop_appium_server(appium_server)
