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

# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--start-maximized")

print("testing started")
driver = webdriver.Chrome(options=options)

def find_scrips():
    all = [f for f in os.listdir('.') if os.path.isfile(f)]
    files = []
    for file in all:
        name, ext = os.path.splitext(file)
        if ext == '.side':
            files.append(file)
            detail = {}
            detail['SPRIDEN_ID'] = name
            ExcelParser.employees.append(detail)
    return files


headers = ExcelParser.init_headers('input.xlsx')
scripts = find_scrips()
# load input report to generate scripts, replace the default script file, execute one by one
if len(scripts) == 0:
    scripts = ExcelParser.generate_side_script('input.xlsx')

# exit(-1)
def run_scripts(scripts):
    for script in scripts:
        try:
            FormBase.script = script
            print(script)

            FormBase.base_url = JsonParser.loadBaseUrl(FormBase.script)

            operations = JsonParser.loadScriptFromJson(FormBase.script)
            # print(operations)
            FormBase.handle(driver, operations)

            # skip removing to avoid missed
            # os.remove(script)
        except:
            print("Error: failed in handling " + script)

        # exit(1)

    ExcelParser.save_results()


if len(scripts) > 0:
    run_scripts(scripts)
# exit(1)

# Close the driver
driver.quit()
