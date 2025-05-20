import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ExcelParser
import os
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
    FormBase.script = 'PDOC.side'

# load input report to generate scripts, replace the default script file, execute one by one
scripts = ExcelParser.generate_side_script('input.xlsx')
for script in scripts:
    try:
        FormBase.script = script
        print(script)

        FormBase.base_url = JsonParser.loadBaseUrl(FormBase.script)

        # Set options for not prompting DevTools information
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--start-maximized")

        print("testing started")
        driver = webdriver.Chrome(options=options)

        operations = JsonParser.loadScriptFromJson(FormBase.script)
        # print(operations)
        FormBase.handle(driver, operations)

        os.remove(script)
    except:
        print("Error: failed in handling " + script)


    # exit(1)

ExcelParser.save_results()
# Close the driver
driver.quit()
