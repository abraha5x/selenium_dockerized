from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import os
from time import sleep



caps = DesiredCapabilities.FIREFOX

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities=caps)
driver.get('https://www.pythonanywhere.com/')

print("Test Passed")



driver.quit()