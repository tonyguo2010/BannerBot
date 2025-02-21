import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from time import sleep

import FormBase

if len(sys.argv) == 3:
    FormBase.working_form = sys.argv[1]
    FormBase.envir = sys.argv[2]
else:
    FormBase.working_form = 'NTRPCLS'
    # exit(-1)


# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--start-maximized")

print("testing started")
driver = webdriver.Chrome(options=options)

# if FormBase.working_form == 'self':
#     driver.get("https://" + FormBase.envir + ".centennialcollege.ca/ssomanager/c/SSB")
# else:
driver.get("https://" + FormBase.envir + ".centennialcollege.ca:7443/applicationNavigator/seamless")

def get_browser_status(driver):
    # myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, '/html/body/nav[5]/div/div[1]/ul/li[3]/h2')))
    return True

def line():
    print('  == ' + str(sys._getframe(1).f_lineno) + ' == ')

while True:
    state = get_browser_status(driver)
    if state is False:
        sleep(3)
        continue
    form_code = FormBase.get_form_code(driver)

    if form_code == 0:
        FormBase.auto_login(driver)
    if form_code == 1:
        FormBase.to_form(driver, FormBase.working_form)
    if form_code == 2:
        FormBase.dispatch_form(driver)
    # if form_code == 3:
    #     FormBase.to_self_service(driver)
    sleep(3)

# Close the driver
driver.quit()
