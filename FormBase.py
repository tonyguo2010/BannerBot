import sys

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

import ExcelParser
import JsonParser


timing = JsonParser.loadJsonFromFile('timing.json')

skips = ['setWindowSize', 'selectFrame']
base_url : str= ''
script : str = ''

def getKey(key):
    if key == 'Space':
        return Keys.SPACE
    elif key == 'Tab':
        return Keys.TAB
    elif key == 'ESC':
        return Keys.ESCAPE
    elif key == '${KEY_ENTER}':
        return Keys.RETURN
    elif key == 'F1':
        return Keys.F1
    elif key == 'F2':
        return Keys.F2
    elif key == 'F3':
        return Keys.F3
    elif key == 'F4':
        return Keys.F4
    elif key == 'F5':
        return Keys.F5
    elif key == 'F6':
        return Keys.F6
    elif key == 'F7':
        return Keys.F7
    elif key == 'F8':
        return Keys.F8
    elif key == 'F9':
        return Keys.F9
    elif key == 'F10':
        return Keys.F10
    elif key == 'Shift':
        return Keys.SHIFT
    elif key == 'Down':
        return Keys.DOWN
    elif key == 'Up':
        return Keys.UP
    elif key == 'End':
        return Keys.END
    elif key == 'Ctrl':
        return Keys.CONTROL
    else:
        return None


def set_input(driver, xpath, value):
    input = driver.find_element(By.XPATH, xpath)
    # input.send_keys(Keys.BACKSPACE)
    input.click()
    sleep(timing['pre_input'])
    input.clear()
    input.send_keys(value)
    sleep(timing['after_input'])


def get_input(driver, xpath):
    input = driver.find_element(By.XPATH, xpath)
    return input.get_attribute('title')


def click_by_xpath(driver, xpath):
    try:
        btn = driver.find_element(By.XPATH, xpath)
        btn.click()
    except Exception as e:
        print("error in clicking " + xpath)
        print(e)
    finally:
        sleep(timing['after_click'])

def click_by_id(driver, id):
    try:
        btn = driver.find_element(By.ID, id)
        btn.click()
    except Exception as e:
        print("error in clicking " + id)
        print(e)
    finally:
        sleep(timing['after_click'])

def select_dropdown_id_text(driver, id, text):
    try:
        select = Select(driver.find_element(By.ID, id))
        select.select_by_visible_text(text)
    except Exception as e:
        print("error in selecting " + id)
        print(e)
    finally:
        sleep(timing['after_select'])

def select_dropdown_text(driver, xpath, text):
    try:
        print(xpath)
        print(text)
        select = Select(driver.find_element(By.XPATH, xpath))
        select.select_by_visible_text(text)
    except Exception as e:
        print("error in selecting " + xpath)
        print(e)
    finally:
        sleep(timing['after_select'])

def select_dropdown(driver, xpath, text):
    try:
        print(xpath)
        print(text)
        select = Select(driver.find_element(By.XPATH, xpath))
        select.select_by_value(text)
    except Exception as e:
        print("error in selecting " + xpath)
        print(e)
    finally:
        sleep(timing['after_select'])


def select_index(driver, xpath, index):
    print('to select index ' + str(index))
    try:
        select = Select(driver.find_element(By.XPATH, xpath))
        select.select_by_index(index)
    except Exception as e:
        print("error in selecting " + xpath)
        print(e)
    finally:
        sleep(timing['after_select'])


def global_key(driver, key):
    sleep(timing['pre_typing'])
    action_key = getKey(key)

    if action_key is not None:
        ActionChains(driver).send_keys(action_key).perform()
    else:
        ActionChains(driver).send_keys(key).perform()
    print(' typing ' + key)
    sleep(timing['after_typing'])

def combo_key(driver, input):
    keys = input.split('-')
    print(keys)
    action = ActionChains(driver)

    for i in range(len(keys)):
        action.key_down(getKey(keys[i]))
    for i in range(len(keys)):
        action.key_up(getKey(keys[i]))

    action.perform()

def get_form_code(driver):
    try:  # login page
        driver.find_element(By.ID, 'usernameUserInput')
        return 0
    except:
        pass

    try:  # normal form
        driver.find_element(By.XPATH, '/html/body/nav[5]/div/div[1]/ul/li[3]/h2')
        return 2
    except:
        pass

    try:
        driver.find_element(By.ID, "search-landing")
        return 1
    except:
        pass

    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[1]/td[1]/h2").text == 'Main Menu'
        return 3
    except:
        pass


def auto_login(driver):
    account = JsonParser.loadJsonFromFile('account.json')
    login_ID = driver.find_element(By.ID, 'usernameUserInput')
    login_pwd = driver.find_element(By.ID, 'password')
    login_ID.send_keys(account['ID'])
    login_pwd.send_keys(account['Password'])
    login_pwd.send_keys(Keys.RETURN)

def to_form(driver, form_name):
    driver.get('https://' + envir + '.centennialcollege.ca:7443/BannerAdmin/?form=' + form_name)


def get_form_name(driver):
    try:
        item = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/form/div[3]/div/div/div[2]/div')
        form_code = item.get_attribute('data-name')

        if form_code is None:
            item = driver.find_element(By.XPATH, '/html/body/nav[5]/div/div[1]/ul/li[3]/h2')
            form_code = item.text

        if form_code is None:
            item = driver.find_element(By.XPATH, '/html/body/nav[5]')
            form_code = item.text

        return form_code
    except:
        pass


def set_input_by_xpath(driver, xpath, value):
    input = driver.find_element(By.XPATH, xpath)
    input.send_keys(Keys.BACKSPACE)
    input.send_keys(Keys.BACKSPACE)
    input.send_keys(Keys.BACKSPACE)
    input.send_keys(Keys.BACKSPACE)
    input.send_keys(Keys.BACKSPACE)
    input.send_keys(Keys.BACKSPACE)
    input.send_keys(Keys.BACKSPACE)
    input.send_keys(Keys.BACKSPACE)
    input.send_keys(Keys.BACKSPACE)
    input.send_keys(Keys.BACKSPACE)
    input.click()
    sleep(timing['pre_input'])
    input.clear()
    input.send_keys(value)
    sleep(timing['after_input'])

def set_input_by_id(driver, id, value):
    print(id)
    print(value)
    input = driver.find_element(By.ID, id)
    # print(input)
    # input.send_keys(Keys.BACKSPACE)
    input.click()
    sleep(timing['pre_input'])
    input.clear()
    print('clear in set_input_by_id')
    input.send_keys(value)
    sleep(timing['after_input'])


def update_employee(employee_id, header, value):
    for employee in ExcelParser.employees:
        if employee['SPRIDEN_ID'] == employee_id:
            employee[header] = value
            break


def get_input_by_xpath(driver, xpath):
    sleep(timing['pre_input'])
    table = driver.find_element(By.XPATH, xpath)
    rows = table.find_elements(By.TAG_NAME, "tr")  # tr elements represent table rows

    # Parse each row
    taxs = []
    for i, row in enumerate(rows):
        cols = row.find_elements(By.TAG_NAME, "td")  # td elements represent table cells
        employee_id = script.removesuffix('.side')

        row_data = []
        if cols[0].text.strip() == 'Federal tax deduction on bonus':
            update_employee(employee_id, 'FED_BONUS_TAX', cols[1].text)
        if cols[0].text.strip() == 'Provincial tax deduction on bonus':
            update_employee(employee_id, 'ONT_BONUS_TAX', cols[1].text)
        if cols[0].text.strip() == 'Total tax deductions on bonus':
            update_employee(employee_id, 'TOT_BONUS_TAX', cols[2].text)
    return taxs
    # return input.get_attribute('title')


def get_input_by_id(driver, id):
    sleep(timing['pre_input'])
    input = driver.find_element(By.ID, id)
    return input.text
    # return input.get_attribute('title')


def click_by_css(driver, css):
    try:
        btn = driver.find_element(By.CSS_SELECTOR, css)
        btn.click()
    except Exception as e:
        print("error in clicking " + css)
        print(e)
    finally:
        sleep(timing['after_click'])


def sendkey_by_css(driver, css, value):
    input = driver.find_element(By.CSS_SELECTOR, css)
    input.click()
    sleep(timing['pre_sendkey'])
    input.send_keys(getKey(value))
    sleep(timing['after_sendkey'])

def sendkey_by_id(driver, id, value):
    input = driver.find_element(By.ID, id)
    # print(input)
    # input.send_keys(Keys.BACKSPACE)
    input.click()
    sleep(timing['pre_sendkey'])
    input.send_keys(getKey(value))
    sleep(timing['after_sendkey'])


def process_operations(driver, operations, header = None, hijack_input = None):
    for operation in operations['commands']:
        if operation['command'] in skips:
            continue
        cmds = operation['target'].split('=')
        print(operation['command'] + ' ' + operation['target'] + ' => ' + operation['value'])

        if operation['command'] == 'type':
            if cmds[0] == 'id':
                if header is not None and header == cmds[1]:
                    set_input_by_id(driver, header, hijack_input)
                else:
                    set_input_by_id(driver, cmds[1], operation['value'])
            elif cmds[0] == 'xpath':
                if header is not None and header == cmds[1]:
                    set_input_by_xpath(driver, header, hijack_input)
                else:
                    set_input_by_xpath(driver, cmds[1], operation['value'])

        elif operation['command'] == 'open':
            driver.get(operation['target'])
            sleep(timing['after_sendkey'])

        elif operation['command'] == 'sendKeys':
            if cmds[0] == 'css':
                sendkey_by_css(driver, cmds[1], operation['value'])
            elif cmds[0] == 'id':
                sendkey_by_id(driver, cmds[1], operation['value'])

        elif operation['command'] == 'click':
            if cmds[0] == 'css':
                click_by_css(driver, cmds[1])
            elif cmds[0] == 'id':
                click_by_id(driver, cmds[1])

        elif operation['command'] == 'select':
            value : str = operation['value']
            if value.startswith('label='):
                value = value.split('=')[1]
                if cmds[0] == 'xpath':
                    select_dropdown_text(driver, cmds[1], value)
                elif cmds[0] == 'id':
                    select_dropdown_id_text(driver, cmds[1], value)
            else:
                if cmds[0] == 'xpath':
                    select_dropdown(driver, cmds[1], operation['value'])

        elif operation['command'] == 'Output':
            value = ''

            if cmds[0] == 'id':
                value = get_input_by_id(driver, cmds[1])
            elif cmds[0] == 'xpath':
                value = get_input_by_xpath(driver, cmds[1])

            print(value)

        elif cmds[0] == 'Glb':
            times = 1
            if 'times' in operation:
                times = operation['times']
            while times > 0:
                global_key(driver, operation['value'])
                times -= 1

        # elif cmds[0] == 'Cmb':
        elif cmds[0] == 'Exit':
            driver.close()
            # sys.exit(0)

def process_operations_old(driver, widgets, operations, header = None, hijack_input = None):
    for operation in operations['opers']:
        print(" updating " + operation['widget'] + ' to ' + operation['value'])
        cmds = operation['widget'].split('_')

        if cmds[0] == 'Input':
            if cmds[1] == 'Path':
                if header is None:
                    set_input_by_xpath(driver, widgets[cmds[2]]['xpath'], operation['value'])
                else:
                    set_input_by_xpath(driver, widgets[header]['xpath'], hijack_input)
            elif cmds[1] == 'ID':
                if header is None:
                    set_input_by_id(driver, widgets[cmds[2]]['id'], operation['value'])
                else:
                    set_input_by_id(driver, widgets[header]['id'], hijack_input)

        elif cmds[0] == 'Btn':
            if cmds[1] == 'Path':
                click_by_xpath(driver, widgets[cmds[2]]['xpath'])
            elif cmds[1] == 'ID':
                click_by_id(driver, widgets[cmds[2]]['id'])

        elif cmds[0] == 'Glb':
            times = 1
            if 'times' in operation:
                times = operation['times']
            while times > 0:
                global_key(driver, operation['value'])
                times -= 1

        # elif cmds[0] == 'Cmb':
        elif cmds[0] == 'Output':
            value = ''

            if cmds[1] == 'Path':
                value = get_input_by_xpath(driver, widgets[cmds[2]]['xpath'])
            elif cmds[1] == 'ID':
                value = get_input_by_id(driver, widgets[cmds[2]]['id'])

            print(value)

        elif cmds[0] == 'Exit':
            driver.close()
            # sys.exit(0)


def handle(driver, operations):
    # try:
        if len(operations['commands']) == 0:
            raise Exception('No operations found')

        '''
          "Excel": {
          "file_name" : "pcls.xlsx",
          "sheet_index" : 0,   // start from 0
          "col_index" : 1      // start from 1
        },
        "commands": [{
          "id": "95faea04-084b-448e-8722-cf8320fa46fa",
          ......
        '''

        file_inputs = []
        if "Excel" in operations:
            file_inputs = ExcelParser.load_list_from_sheet_by_col(
                operations['Excel']['file_name'],
                operations['Excel']['sheet_index'],
                operations['Excel']['col_index']
            )
        print(file_inputs)

        if len(file_inputs) > 0:
            index = 0
            header = ''
            for hijack in file_inputs:
                index += 1
                if index == 1:
                    header = hijack
                    continue
                process_operations(driver, operations, header, hijack)
        else:
            process_operations(driver, operations)
