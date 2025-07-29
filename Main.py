import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from time import sleep

import FormBase
import JsonParser

if len(sys.argv) == 2:
    FormBase.script = sys.argv[1]
else:
    FormBase.script = 'EM001-EM005.side'

FormBase.base_url = JsonParser.loadBaseUrl(FormBase.script)

# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--start-maximized")

print("testing started")
driver = webdriver.Chrome(options=options)

# driver.get(FormBase.base_url)

driver.get('https://tprdn.centennialcollege.ca/applicationNavigator')
sleep(2)
FormBase.auto_login(driver)
sleep(5)

operations = JsonParser.loadScriptFromJson(FormBase.script)
# print(operations)
FormBase.handle(driver, operations)

# Close the driver
driver.quit()
