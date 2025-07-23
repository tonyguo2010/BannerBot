import ScriptLib

def preload(file):
    commands = []

    commands.append(ScriptLib.command_target_value("open", "https://apps.cra-arc.gc.ca/ebci/rhpd/beta/entry", ""))
    commands.append(ScriptLib.command_target_value("setWindowSize", "1920x1016", ""))
    commands.append(ScriptLib.command_target_value("click", "css=.navigation_button", ""))
    commands.append(ScriptLib.command_target_value("click", "xpath=//select", ""))
    commands.append(ScriptLib.command_target_value("select", "xpath=//select", "label=Ontario"))
    commands.append(ScriptLib.command_target_value("click", "css=optgroup > option:nth-child(7)", ""))
    commands.append(ScriptLib.command_target_value("click", "xpath=//rccr-select[2]/div/select", ""))
    commands.append(ScriptLib.command_target_value("select", "xpath=/html/body/app-root/rccr-wet-template/div/div/main/app-step1/form/rccr-select[2]/div/select", "label=Biweekly (27 pay periods a year)"))
    commands.append(ScriptLib.command_target_value("click", "id=datePaidYear", ""))
    commands.append(ScriptLib.command_target_value("select", "id=datePaidYear", "label=2025"))
    commands.append(ScriptLib.command_target_value("click", "xpath=//option[@value='2025']", ""))
    commands.append(ScriptLib.command_target_value("click", "xpath=//div/rccr-select[2]/div/select", ""))
    commands.append(ScriptLib.command_target_value("select", "xpath=/html/body/app-root/rccr-wet-template/div/div/main/app-step1/form/fieldset/div[2]/div/div/rccr-select[2]/div/select", "label=July"))
    commands.append(ScriptLib.command_target_value("click", "xpath=//div/rccr-select[2]/div/select/option[3]", ""))
    commands.append(ScriptLib.command_target_value("click", "xpath=//rccr-select[3]/div/select", ""))
    commands.append(ScriptLib.command_target_value("select", "xpath=//rccr-select[3]/div/select", "label=01"))
    commands.append(ScriptLib.command_target_value("click", "xpath=//rccr-select[3]/div/select/option[2]", ""))
    commands.append(ScriptLib.command_target_value("click", "css=.next", ""))

    file.write(','.join(commands))

def preload_old(file):
    file.write('''
    {
      "id": "566c9ccb-bb48-44c0-bfbb-ac17dbf17f94",
      "comment": "",
      "command": "open",
      "target": "https://apps.cra-arc.gc.ca/ebci/rhpd/beta/entry",
      "targets": [],
      "value": ""
    }, 	
{
      "id": "107dc0b0-68ff-46da-9853-8f342a981533",
      "comment": "",
      "command": "setWindowSize",
      "target": "1920x1016",
      "targets": [],
      "value": ""
    }, 	
{
      "id": "aa86756b-e92a-4e8c-a877-c8d887ccf1b8",
      "comment": "",
      "command": "click",
      "target": "css=.navigation_button",
      "targets": [
        ["css=.navigation_button", "css:finder"],
        ["xpath=//button", "xpath:position"],
        ["xpath=//button[contains(.,'Next')]", "xpath:innerText"]
      ],
      "value": ""
    }, 	
{
      "id": "0e61fb34-146e-4404-9d8b-3757e1befe72",
      "comment": "",
      "command": "click",
      "target": "xpath=//select",
      "targets": [
        ["id=08bb9db7-4f0c-de33-db90-7079bbf7f35d", "id"],
        ["css=#\\\\30 8bb9db7-4f0c-de33-db90-7079bbf7f35d", "css:finder"],
        ["xpath=//select[@id='08bb9db7-4f0c-de33-db90-7079bbf7f35d']", "xpath:attributes"],
        ["xpath=//select", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "07def488-cc1d-4f55-8fa6-616772de7a70",
      "comment": "",
      "command": "select",
      "target": "xpath=//select",
      "targets": [],
      "value": "label=Ontario"
    }, 	
{
      "id": "1c4a1034-9686-4723-9bb9-2838ef0588c3",
      "comment": "",
      "command": "click",
      "target": "css=optgroup > option:nth-child(7)",
      "targets": [
        ["css=optgroup > option:nth-child(7)", "css:finder"],
        ["xpath=//option[@value='ONTARIO']", "xpath:attributes"],
        ["xpath=//select[@id='08bb9db7-4f0c-de33-db90-7079bbf7f35d']/optgroup/option[7]", "xpath:idRelative"],
        ["xpath=//option[7]", "xpath:position"],
        ["xpath=//option[contains(.,' Ontario ')]", "xpath:innerText"]
      ],
      "value": ""
    }, 	
{
      "id": "8eff9aae-5764-4c8d-8efe-0fe90902a0ca",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-select[2]/div/select",
      "targets": [
        ["id=2aaa4369-0788-21e2-4c3c-0e92efe8d664", "id"],
        ["css=#\\\\32 aaa4369-0788-21e2-4c3c-0e92efe8d664", "css:finder"],
        ["xpath=//select[@id='2aaa4369-0788-21e2-4c3c-0e92efe8d664']", "xpath:attributes"],
        ["xpath=//rccr-select[2]/div/select", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "8e879673-60f9-4b8e-aaa7-3b15f104f0a5",
      "comment": "",
      "command": "select",
      "target": "xpath=/html/body/app-root/rccr-wet-template/div/div/main/app-step1/form/rccr-select[2]/div/select",
      "targets": [],
      "value": "label=Biweekly (27 pay periods a year)"
    }, 	
{
      "id": "743b16d6-4655-4ea7-8167-f681652dd76f",
      "comment": "",
      "command": "click",
      "target": "id=datePaidYear",
      "targets": [
        ["id=datePaidYear", "id"],
        ["css=#datePaidYear", "css:finder"],
        ["xpath=//select[@id='datePaidYear']", "xpath:attributes"],
        ["xpath=//div/rccr-select/div/select", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "710b91aa-c051-4ae8-8585-4ae30d361a66",
      "comment": "",
      "command": "select",
      "target": "id=datePaidYear",
      "targets": [],
      "value": "label=2025"
    }, 	
{
      "id": "91501171-cc30-40b6-bc37-272f811a8e99",
      "comment": "",
      "command": "click",
      "target": "xpath=//option[@value='2025']",
      "targets": [
        ["css=#datePaidYear > option:nth-child(2)", "css:finder"],
        ["xpath=//option[@value='2025']", "xpath:attributes"],
        ["xpath=//select[@id='datePaidYear']/option[2]", "xpath:idRelative"],
        ["xpath=//div/rccr-select/div/select/option[2]", "xpath:position"],
        ["xpath=//option[contains(.,'2025')]", "xpath:innerText"]
      ],
      "value": ""
    }, 	
{
      "id": "3065d90f-9218-4976-88e9-f486f7d87df8",
      "comment": "",
      "command": "click",
      "target": "xpath=//div/rccr-select[2]/div/select",
      "targets": [
        ["id=8905f49f-b13f-e0bc-2e11-57a3012a1a44", "id"],
        ["css=#\\\\38 905f49f-b13f-e0bc-2e11-57a3012a1a44", "css:finder"],
        ["xpath=//select[@id='8905f49f-b13f-e0bc-2e11-57a3012a1a44']", "xpath:attributes"],
        ["xpath=//div/rccr-select[2]/div/select", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "3fe71756-bd31-4611-a68b-22db8dd47fe0",
      "comment": "",
      "command": "select",
      "target": "xpath=/html/body/app-root/rccr-wet-template/div/div/main/app-step1/form/fieldset/div[2]/div/div/rccr-select[2]/div/select",
      "targets": [],
      "value": "label=February"
    }, 	
{
      "id": "d281c865-9e3e-4877-b120-187441a3f685",
      "comment": "",
      "command": "click",
      "target": "xpath=//div/rccr-select[2]/div/select/option[3]",
      "targets": [
        ["css=#\\\\38 905f49f-b13f-e0bc-2e11-57a3012a1a44 > option:nth-child(3)", "css:finder"],
        ["xpath=//option[@value='02']", "xpath:attributes"],
        ["xpath=//select[@id='8905f49f-b13f-e0bc-2e11-57a3012a1a44']/option[3]", "xpath:idRelative"],
        ["xpath=//div/rccr-select[2]/div/select/option[3]", "xpath:position"],
        ["xpath=//option[contains(.,'February')]", "xpath:innerText"]
      ],
      "value": ""
    }, 	
{
      "id": "88d137ed-1d4d-47c7-b9fd-2e5e28bd3a54",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-select[3]/div/select",
      "targets": [
        ["id=6d213f40-1f06-c40b-6764-3614142d6928", "id"],
        ["css=#\\\\36 d213f40-1f06-c40b-6764-3614142d6928", "css:finder"],
        ["xpath=//select[@id='6d213f40-1f06-c40b-6764-3614142d6928']", "xpath:attributes"],
        ["xpath=//rccr-select[3]/div/select", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "ba692303-00ef-4939-8e9a-d9185314ff25",
      "comment": "",
      "command": "select",
      "target": "xpath=//rccr-select[3]/div/select",
      "targets": [],
      "value": "label=01"
    }, 	
{
      "id": "70bd2942-e97a-4736-b676-df2f0d29423d",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-select[3]/div/select/option[2]",
      "targets": [
        ["css=#\\\\36 d213f40-1f06-c40b-6764-3614142d6928 > option:nth-child(2)", "css:finder"],
        ["xpath=(//option[@value='01'])[2]", "xpath:attributes"],
        ["xpath=//select[@id='6d213f40-1f06-c40b-6764-3614142d6928']/option[2]", "xpath:idRelative"],
        ["xpath=//rccr-select[3]/div/select/option[2]", "xpath:position"],
        ["xpath=//option[contains(.,'01')]", "xpath:innerText"]
      ],
      "value": ""
    }, 	
{
      "id": "3f8e3da8-8bdf-416c-89a8-0762c65592ba",
      "comment": "",
      "command": "click",
      "target": "css=.next",
      "targets": [
        ["css=.next", "css:finder"],
        ["xpath=//button", "xpath:position"],
        ["xpath=//button[contains(.,'Next')]", "xpath:innerText"]
      ],
      "value": ""
    }
    ''')

def validate_value(value, default = False):
    if value == None:
        return ""
    if type(value) == int or type(value) == float:
        if value == 0:
            return ""
        if default == False:
            return str('%.2f' % value)
        else:
            return str(value)
    return value

def incomes(file, detail):
    commands = []

    # commands.append(ScriptLib.command_target_value("click", "xpath=//input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//input",  validate_value(detail['RGER_PAY'])))

    commands.append(ScriptLib.command_target_value("click", "css=.ng-untouched:nth-child(2) > .radio > .form-radio", ""))
    # commands.append(ScriptLib.command_target_value("click", "xpath=//div/rccr-currency-input/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//div/rccr-currency-input/div/div/input",  validate_value(detail['LSPM_AMT'])))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//div/rccr-currency-input[2]/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//div/rccr-currency-input[2]/div/div/input",  validate_value(detail['CAAT_ON_LSM_AMT'])))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//rccr-currency-input[3]/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//rccr-currency-input[3]/div/div/input",  validate_value(detail['LYTD_AMT'])))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//rccr-currency-input[4]/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//rccr-currency-input[4]/div/div/input",  validate_value(detail['YTD_CAL_EE_AMT'])))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//rccr-currency-input[5]/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//rccr-currency-input[5]/div/div/input",  ""))

    commands.append(ScriptLib.command_target_value("click", "css=.mrgn-bttm-md > .ng-untouched label > span:nth-child(2)", ""))
    # commands.append(ScriptLib.command_target_value("click", "xpath=//div/fieldset/rccr-currency-input/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//div/fieldset/rccr-currency-input/div/div/input",  validate_value(detail['TBCH_AMT'])))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//div/fieldset/rccr-currency-input[2]/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//div/fieldset/rccr-currency-input[2]/div/div/input",  ""))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//fieldset/rccr-currency-input[3]/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//fieldset/rccr-currency-input[3]/div/div/input",  validate_value(detail['TBNC_AMT'])))

    commands.append(ScriptLib.command_target_value("click", "css=.ng-untouched:nth-child(1) > .checkbox span", ""))
    # commands.append(ScriptLib.command_target_value("click", "xpath=//fieldset[3]/div/div/fieldset/rccr-currency-input/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//fieldset[3]/div/div/fieldset/rccr-currency-input/div/div/input",  ""))

    commands.append(ScriptLib.command_target_value("click", "css=.ng-untouched:nth-child(3) > .checkbox span:nth-child(2)", ""))
    # commands.append(ScriptLib.command_target_value("click", "xpath=//div[2]/fieldset/rccr-currency-input[2]/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//div[2]/fieldset/rccr-currency-input[2]/div/div/input",  validate_value(detail['CAAT_ON_REG_AMT'])))

    commands.append(ScriptLib.command_target_value("click", "css=.ng-untouched:nth-child(5) label", ""))
    # commands.append(ScriptLib.command_target_value("click", "xpath=//div[3]/fieldset/rccr-currency-input/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//div[3]/fieldset/rccr-currency-input/div/div/input",  validate_value(detail['CP_TOT_UN'])))

    commands.append(ScriptLib.command_target_value("click", "css=.ng-untouched:nth-child(7) label > span:nth-child(2)", ""))
    # commands.append(ScriptLib.command_target_value("click", "xpath=//div[4]/fieldset/rccr-currency-input/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//div[4]/fieldset/rccr-currency-input/div/div/input",  validate_value(detail['FED_PRS_ZON'])))

    commands.append(ScriptLib.command_target_value("click", "css=.next", ""))

    file.write(',' + ','.join(commands))
def incomes_old(file, detail):
    if detail['RGER_PAY'] is not None:
        file.write(''',{
      "id": "620ab309-3311-4896-a21e-c683fe7a3428",
      "comment": "",
      "command": "click",
      "target": "xpath=//input",
      "targets": [
        ["id=ba3b0ee9-ce05-6554-4f8f-faa6f1d95ab8", "id"],
        ["css=#ba3b0ee9-ce05-6554-4f8f-faa6f1d95ab8", "css:finder"],
        ["xpath=//input[@id='ba3b0ee9-ce05-6554-4f8f-faa6f1d95ab8']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "4d7fe47a-b48c-493c-9bae-acac0aafa870",
      "comment": "",
      "command": "type",
      "target": "xpath=//input",
      "targets": [
        ["id=ba3b0ee9-ce05-6554-4f8f-faa6f1d95ab8", "id"],
        ["css=#ba3b0ee9-ce05-6554-4f8f-faa6f1d95ab8", "css:finder"],
        ["xpath=//input[@id='ba3b0ee9-ce05-6554-4f8f-faa6f1d95ab8']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['RGER_PAY'])  + '''"
    }''')

    if detail['LSPM_AMT'] is not None:
        file.write(''',{
      "id": "41608209-4a58-4f41-a4cd-ec8e2cefa648",
      "comment": "",
      "command": "runScript",
      "target": "window.scrollTo(0,0)",
      "targets": [],
      "value": ""
    }, 	
{
      "id": "145e057b-df1c-451f-8460-d78f181fe87d",
      "comment": "",
      "command": "click",
      "target": "css=.ng-untouched:nth-child(2) > .radio > .form-radio",
      "targets": [
        ["css=.ng-untouched:nth-child(2) > .radio > .form-radio", "css:finder"],
        ["xpath=//div/label", "xpath:position"],
        ["xpath=//label[contains(.,'A bonus payment')]", "xpath:innerText"]
      ],
      "value": ""
    }, 	
{
      "id": "9402db56-c4a4-441d-b517-43be234e4f4e",
      "comment": "",
      "command": "click",
      "target": "xpath=//div/rccr-currency-input/div/div/input",
      "targets": [
        ["id=d53daf64-1a05-6394-e526-2977c2f15838", "id"],
        ["css=#d53daf64-1a05-6394-e526-2977c2f15838", "css:finder"],
        ["xpath=//input[@id='d53daf64-1a05-6394-e526-2977c2f15838']", "xpath:attributes"],
        ["xpath=//div/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "94080ba5-f9f2-4831-a29b-577d4618c301",
      "comment": "",
      "command": "type",
      "target": "xpath=//div/rccr-currency-input/div/div/input",
      "targets": [
        ["id=d53daf64-1a05-6394-e526-2977c2f15838", "id"],
        ["css=#d53daf64-1a05-6394-e526-2977c2f15838", "css:finder"],
        ["xpath=//input[@id='d53daf64-1a05-6394-e526-2977c2f15838']", "xpath:attributes"],
        ["xpath=//div/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['LSPM_AMT']) + '''"
    }, 	
{
      "id": "f5fd5df1-ca3e-4f72-99ca-681a36ec930b",
      "comment": "",
      "command": "click",
      "target": "xpath=//div/rccr-currency-input[2]/div/div/input",
      "targets": [
        ["id=6edc5d82-d13b-1db4-8720-099f96ba563c", "id"],
        ["css=#\\\\36 edc5d82-d13b-1db4-8720-099f96ba563c", "css:finder"],
        ["xpath=//input[@id='6edc5d82-d13b-1db4-8720-099f96ba563c']", "xpath:attributes"],
        ["xpath=//div/rccr-currency-input[2]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "1f02f850-9bbc-4ecd-a453-3da7b2dfbeb9",
      "comment": "",
      "command": "type",
      "target": "xpath=//div/rccr-currency-input[2]/div/div/input",
      "targets": [
        ["id=6edc5d82-d13b-1db4-8720-099f96ba563c", "id"],
        ["css=#\\\\36 edc5d82-d13b-1db4-8720-099f96ba563c", "css:finder"],
        ["xpath=//input[@id='6edc5d82-d13b-1db4-8720-099f96ba563c']", "xpath:attributes"],
        ["xpath=//div/rccr-currency-input[2]/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['CAAT_ON_LSM_AMT']) + '''"
    }, 	
{
      "id": "0f926827-27ad-496a-99fb-25d718dd8452",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-currency-input[3]/div/div/input",
      "targets": [
        ["id=9c8f5caa-cb5d-8c1a-e7b1-fcd995810408", "id"],
        ["css=#\\\\39 c8f5caa-cb5d-8c1a-e7b1-fcd995810408", "css:finder"],
        ["xpath=//input[@id='9c8f5caa-cb5d-8c1a-e7b1-fcd995810408']", "xpath:attributes"],
        ["xpath=//rccr-currency-input[3]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "ef7bd2a9-c69d-42d4-a06f-8c68a7c9991b",
      "comment": "",
      "command": "type",
      "target": "xpath=//rccr-currency-input[3]/div/div/input",
      "targets": [
        ["id=9c8f5caa-cb5d-8c1a-e7b1-fcd995810408", "id"],
        ["css=#\\\\39 c8f5caa-cb5d-8c1a-e7b1-fcd995810408", "css:finder"],
        ["xpath=//input[@id='9c8f5caa-cb5d-8c1a-e7b1-fcd995810408']", "xpath:attributes"],
        ["xpath=//rccr-currency-input[3]/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['LYTD_AMT']) + '''"
    }, 	
{
      "id": "0f926827-27ad-496a-99fb-25d718dd8452",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-currency-input[4]/div/div/input",
      "targets": [
        ["id=9c8f5caa-cb5d-8c1a-e7b1-fcd995810408", "id"],
        ["css=#\\\\39 c8f5caa-cb5d-8c1a-e7b1-fcd995810408", "css:finder"],
        ["xpath=//input[@id='9c8f5caa-cb5d-8c1a-e7b1-fcd995810408']", "xpath:attributes"],
        ["xpath=//rccr-currency-input[4]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "ef7bd2a9-c69d-42d4-a06f-8c68a7c9991b",
      "comment": "",
      "command": "type",
      "target": "xpath=//rccr-currency-input[4]/div/div/input",
      "targets": [
        ["id=9c8f5caa-cb5d-8c1a-e7b1-fcd995810408", "id"],
        ["css=#\\\\39 c8f5caa-cb5d-8c1a-e7b1-fcd995810408", "css:finder"],
        ["xpath=//input[@id='9c8f5caa-cb5d-8c1a-e7b1-fcd995810408']", "xpath:attributes"],
        ["xpath=//rccr-currency-input[4]/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['YTD_CAL_EE_AMT']) + '''"
    }, 	
{
      "id": "6cff2f18-d4a8-43c8-a94e-2a83ad49af96",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-currency-input[5]/div/div/input",
      "targets": [
        ["id=57f8957e-ef58-f2ff-9eec-15a9bce19476", "id"],
        ["css=#\\\\35 7f8957e-ef58-f2ff-9eec-15a9bce19476", "css:finder"],
        ["xpath=//input[@id='57f8957e-ef58-f2ff-9eec-15a9bce19476']", "xpath:attributes"],
        ["xpath=//rccr-currency-input[5]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "42fa64af-bec7-4920-a774-eba6a534a5ab",
      "comment": "",
      "command": "type",
      "target": "xpath=//rccr-currency-input[5]/div/div/input",
      "targets": [
        ["id=57f8957e-ef58-f2ff-9eec-15a9bce19476", "id"],
        ["css=#\\\\35 7f8957e-ef58-f2ff-9eec-15a9bce19476", "css:finder"],
        ["xpath=//input[@id='57f8957e-ef58-f2ff-9eec-15a9bce19476']", "xpath:attributes"],
        ["xpath=//rccr-currency-input[5]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }''')

    if detail['TBCH_AMT'] is not None or detail['TBNC_AMT'] is not None:
        file.write(''', 	{
      "id": "fcc43efc-a7bc-4a51-9f2e-4a7e2a220a56",
      "comment": "",
      "command": "click",
      "target": "css=.mrgn-bttm-md > .ng-untouched label > span:nth-child(2)",
      "targets": [
        ["css=.mrgn-bttm-md > .ng-untouched label > span:nth-child(2)", "css:finder"],
        ["xpath=//div/label/span", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "b4fd1927-195a-4b62-974a-334e0ff96cad",
      "comment": "",
      "command": "click",
      "target": "xpath=//div/fieldset/rccr-currency-input/div/div/input",
      "targets": [
        ["id=4da18e21-eb07-2224-8fdf-3e6c586bf2cb", "id"],
        ["css=#\\\\34 da18e21-eb07-2224-8fdf-3e6c586bf2cb", "css:finder"],
        ["xpath=//input[@id='4da18e21-eb07-2224-8fdf-3e6c586bf2cb']", "xpath:attributes"],
        ["xpath=//div/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "688d77d4-fc0b-45fe-ab1b-ae33009cadfd",
      "comment": "",
      "command": "type",
      "target": "xpath=//div/fieldset/rccr-currency-input/div/div/input",
      "targets": [
        ["id=4da18e21-eb07-2224-8fdf-3e6c586bf2cb", "id"],
        ["css=#\\\\34 da18e21-eb07-2224-8fdf-3e6c586bf2cb", "css:finder"],
        ["xpath=//input[@id='4da18e21-eb07-2224-8fdf-3e6c586bf2cb']", "xpath:attributes"],
        ["xpath=//div/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['TBCH_AMT']) + '''"
    }, 	
{
      "id": "a5f2cc35-c29f-486e-8c6d-96dafd10dbb8",
      "comment": "",
      "command": "click",
      "target": "xpath=//div/fieldset/rccr-currency-input[2]/div/div/input",
      "targets": [
        ["id=6c5d3271-81ad-db9c-c508-717ac0af3420", "id"],
        ["css=#\\\\36 c5d3271-81ad-db9c-c508-717ac0af3420", "css:finder"],
        ["xpath=//input[@id='6c5d3271-81ad-db9c-c508-717ac0af3420']", "xpath:attributes"],
        ["xpath=//div/fieldset/rccr-currency-input[2]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "25ff75bf-c308-4d3a-86a0-c83fb160239a",
      "comment": "",
      "command": "type",
      "target": "xpath=//div/fieldset/rccr-currency-input[2]/div/div/input",
      "targets": [
        ["id=6c5d3271-81ad-db9c-c508-717ac0af3420", "id"],
        ["css=#\\\\36 c5d3271-81ad-db9c-c508-717ac0af3420", "css:finder"],
        ["xpath=//input[@id='6c5d3271-81ad-db9c-c508-717ac0af3420']", "xpath:attributes"],
        ["xpath=//div/fieldset/rccr-currency-input[2]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "03dc1738-ed22-4aec-92e5-7cc1f49773c0",
      "comment": "",
      "command": "click",
      "target": "xpath=//fieldset/rccr-currency-input[3]/div/div/input",
      "targets": [
        ["id=cec15b8b-a57a-6f9a-9f12-1861ba6680c4", "id"],
        ["css=#cec15b8b-a57a-6f9a-9f12-1861ba6680c4", "css:finder"],
        ["xpath=//input[@id='cec15b8b-a57a-6f9a-9f12-1861ba6680c4']", "xpath:attributes"],
        ["xpath=//fieldset/rccr-currency-input[3]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "27786e07-a83d-42f6-9fe8-962eec693052",
      "comment": "",
      "command": "type",
      "target": "xpath=//fieldset/rccr-currency-input[3]/div/div/input",
      "targets": [
        ["id=cec15b8b-a57a-6f9a-9f12-1861ba6680c4", "id"],
        ["css=#cec15b8b-a57a-6f9a-9f12-1861ba6680c4", "css:finder"],
        ["xpath=//input[@id='cec15b8b-a57a-6f9a-9f12-1861ba6680c4']", "xpath:attributes"],
        ["xpath=//fieldset/rccr-currency-input[3]/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['TBNC_AMT']) + '''"
    }'''
        )
    if True: #  Employer's contributions to the employee's RRSP
        file.write('''
, 	
{
      "id": "9915529c-151a-4838-9e8f-3cf4ff0cf611",
      "comment": "",
      "command": "click",
      "target": "css=.ng-untouched:nth-child(1) > .checkbox span",
      "targets": [
        ["css=.ng-untouched:nth-child(1) > .checkbox span", "css:finder"],
        ["xpath=//fieldset[3]/div/rccr-checkbox/div/label/span", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "09280d13-e960-4984-97f3-6fea623745fa",
      "comment": "",
      "command": "click",
      "target": "xpath=//fieldset[3]/div/div/fieldset/rccr-currency-input/div/div/input",
      "targets": [
        ["id=49b8a63d-238d-0f88-45bb-453b8d222d5d", "id"],
        ["css=#\\\\34 9b8a63d-238d-0f88-45bb-453b8d222d5d", "css:finder"],
        ["xpath=//input[@id='49b8a63d-238d-0f88-45bb-453b8d222d5d']", "xpath:attributes"],
        ["xpath=//fieldset[3]/div/div/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "ae9cff7d-e364-4f25-b92b-28f6379c8773",
      "comment": "",
      "command": "type",
      "target": "xpath=//fieldset[3]/div/div/fieldset/rccr-currency-input/div/div/input",
      "targets": [
        ["id=49b8a63d-238d-0f88-45bb-453b8d222d5d", "id"],
        ["css=#\\\\34 9b8a63d-238d-0f88-45bb-453b8d222d5d", "css:finder"],
        ["xpath=//input[@id='49b8a63d-238d-0f88-45bb-453b8d222d5d']", "xpath:attributes"],
        ["xpath=//fieldset[3]/div/div/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": ""
    }        ''')

    if True or detail['CAAT_ON_REG_AMT'] is not None:
        file.write('''
        , 	
{
      "id": "c3a9217b-bdec-4093-9b09-d5e02083b07f",
      "comment": "",
      "command": "click",
      "target": "css=.ng-untouched:nth-child(3) > .checkbox span:nth-child(2)",
      "targets": [
        ["css=.ng-untouched:nth-child(3) > .checkbox span:nth-child(2)", "css:finder"],
        ["xpath=//rccr-checkbox[2]/div/label/span", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "d87e3081-fe7c-4d08-bb6e-b42eede7a728",
      "comment": "",
      "command": "click",
      "target": "xpath=//div[2]/fieldset/rccr-currency-input[2]/div/div/input",
      "targets": [
        ["id=8a64f03c-e7a6-09f4-3d32-65850e9dd1dd", "id"],
        ["css=#\\\\38 a64f03c-e7a6-09f4-3d32-65850e9dd1dd", "css:finder"],
        ["xpath=//input[@id='8a64f03c-e7a6-09f4-3d32-65850e9dd1dd']", "xpath:attributes"],
        ["xpath=//div[2]/fieldset/rccr-currency-input[2]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "a156aea3-b9e7-4708-b5d3-e1eb1d8f5aed",
      "comment": "",
      "command": "type",
      "target": "xpath=//div[2]/fieldset/rccr-currency-input[2]/div/div/input",
      "targets": [
        ["id=8a64f03c-e7a6-09f4-3d32-65850e9dd1dd", "id"],
        ["css=#\\\\38 a64f03c-e7a6-09f4-3d32-65850e9dd1dd", "css:finder"],
        ["xpath=//input[@id='8a64f03c-e7a6-09f4-3d32-65850e9dd1dd']", "xpath:attributes"],
        ["xpath=//div[2]/fieldset/rccr-currency-input[2]/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['CAAT_ON_REG_AMT']) + '''"
    }''')
    if True or detail['CP_TOT_UN'] is not None:
        file.write('''
, 	
{
      "id": "9cd0352d-a1d0-40a5-a178-02bc59dc5c38",
      "comment": "",
      "command": "click",
      "target": "css=.ng-untouched:nth-child(5) label",
      "targets": [
        ["css=.ng-untouched:nth-child(5) label", "css:finder"],
        ["xpath=//rccr-checkbox[3]/div/label", "xpath:position"],
        ["xpath=//label[contains(.,'Union dues')]", "xpath:innerText"]
      ],
      "value": ""
    }, 	
{
      "id": "119bd151-d53a-4003-b404-86407cad0564",
      "comment": "",
      "command": "click",
      "target": "xpath=//div[3]/fieldset/rccr-currency-input/div/div/input",
      "targets": [
        ["id=78a2ca94-1126-4568-e8f0-8dddd002a33e", "id"],
        ["css=#\\\\37 8a2ca94-1126-4568-e8f0-8dddd002a33e", "css:finder"],
        ["xpath=//input[@id='78a2ca94-1126-4568-e8f0-8dddd002a33e']", "xpath:attributes"],
        ["xpath=//div[3]/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "c66aede6-4d6d-4257-a550-e09de64821b6",
      "comment": "",
      "command": "type",
      "target": "xpath=//div[3]/fieldset/rccr-currency-input/div/div/input",
      "targets": [
        ["id=78a2ca94-1126-4568-e8f0-8dddd002a33e", "id"],
        ["css=#\\\\37 8a2ca94-1126-4568-e8f0-8dddd002a33e", "css:finder"],
        ["xpath=//input[@id='78a2ca94-1126-4568-e8f0-8dddd002a33e']", "xpath:attributes"],
        ["xpath=//div[3]/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['CP_TOT_UN']) + '''"
    }        ''')
    if True or detail['FED_PRS_ZON'] is not None:
        file.write('''
        , 	
{
      "id": "704b88ed-613f-4b95-9db1-8e2319ff6979",
      "comment": "",
      "command": "click",
      "target": "css=.ng-untouched:nth-child(7) label > span:nth-child(2)",
      "targets": [
        ["css=.ng-untouched:nth-child(7) label > span:nth-child(2)", "css:finder"],
        ["xpath=//rccr-checkbox[4]/div/label/span", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "ab9e1ccd-6bbf-4039-9745-6d9a8768cb3b",
      "comment": "",
      "command": "click",
      "target": "xpath=//div[4]/fieldset/rccr-currency-input/div/div/input",
      "targets": [
        ["id=9806f3fc-68c1-aa4b-b7fa-c79e6c49d43f", "id"],
        ["css=#\\\\39 806f3fc-68c1-aa4b-b7fa-c79e6c49d43f", "css:finder"],
        ["xpath=//input[@id='9806f3fc-68c1-aa4b-b7fa-c79e6c49d43f']", "xpath:attributes"],
        ["xpath=//div[4]/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "e7ea69d0-f771-443a-bdb4-b7bc58d30d6d",
      "comment": "",
      "command": "type",
      "target": "xpath=//div[4]/fieldset/rccr-currency-input/div/div/input",
      "targets": [
        ["id=9806f3fc-68c1-aa4b-b7fa-c79e6c49d43f", "id"],
        ["css=#\\\\39 806f3fc-68c1-aa4b-b7fa-c79e6c49d43f", "css:finder"],
        ["xpath=//input[@id='9806f3fc-68c1-aa4b-b7fa-c79e6c49d43f']", "xpath:attributes"],
        ["xpath=//div[4]/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['FED_PRS_ZON']) + '''"
    }''')

#     if True: # support kids and disables
#         file.write('''
#         ,
# {
#       "id": "cefbc65e-f468-4c25-8368-b406d51cb8de",
#       "comment": "",
#       "command": "click",
#       "target": "css=.ng-untouched:nth-child(9) span",
#       "targets": [
#         ["css=.ng-untouched:nth-child(9) span", "css:finder"],
#         ["xpath=//rccr-checkbox[5]/div/label/span", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "11cb88dd-0627-4e5d-ad9d-2dafb5d326fc",
#       "comment": "",
#       "command": "click",
#       "target": "xpath=//rccr-integer-input/div/div/input",
#       "targets": [
#         ["id=dec20f08-15c0-8f4b-8cd4-e9d2a8c627fd", "id"],
#         ["css=#dec20f08-15c0-8f4b-8cd4-e9d2a8c627fd", "css:finder"],
#         ["xpath=//input[@id='dec20f08-15c0-8f4b-8cd4-e9d2a8c627fd']", "xpath:attributes"],
#         ["xpath=//rccr-integer-input/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "8cb5c62f-e61f-4376-8a54-d31aa51fdca0",
#       "comment": "",
#       "command": "type",
#       "target": "xpath=//rccr-integer-input/div/div/input",
#       "targets": [
#         ["id=dec20f08-15c0-8f4b-8cd4-e9d2a8c627fd", "id"],
#         ["css=#dec20f08-15c0-8f4b-8cd4-e9d2a8c627fd", "css:finder"],
#         ["xpath=//input[@id='dec20f08-15c0-8f4b-8cd4-e9d2a8c627fd']", "xpath:attributes"],
#         ["xpath=//rccr-integer-input/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "2c61540e-e30e-4856-8b8f-d86a0269e028",
#       "comment": "",
#       "command": "click",
#       "target": "xpath=//rccr-integer-input[2]/div/div/input",
#       "targets": [
#         ["id=4e9b74ad-450a-15a4-dd4c-434e590926d6", "id"],
#         ["css=#\\\\34 e9b74ad-450a-15a4-dd4c-434e590926d6", "css:finder"],
#         ["xpath=//input[@id='4e9b74ad-450a-15a4-dd4c-434e590926d6']", "xpath:attributes"],
#         ["xpath=//rccr-integer-input[2]/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "27703cff-f5bf-4ba7-b5aa-0088a42db248",
#       "comment": "",
#       "command": "type",
#       "target": "xpath=//rccr-integer-input[2]/div/div/input",
#       "targets": [
#         ["id=4e9b74ad-450a-15a4-dd4c-434e590926d6", "id"],
#         ["css=#\\\\34 e9b74ad-450a-15a4-dd4c-434e590926d6", "css:finder"],
#         ["xpath=//input[@id='4e9b74ad-450a-15a4-dd4c-434e590926d6']", "xpath:attributes"],
#         ["xpath=//rccr-integer-input[2]/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     }''')
#     if True: # Alimony
#         file.write(''',
# {
#       "id": "278e0b6e-fd84-4ad7-8086-048bbc056870",
#       "comment": "",
#       "command": "click",
#       "target": "css=.ng-untouched:nth-child(11) label > span:nth-child(2)",
#       "targets": [
#         ["css=.ng-untouched:nth-child(11) label > span:nth-child(2)", "css:finder"],
#         ["xpath=//rccr-checkbox[6]/div/label/span", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "a801f103-27f9-4cfc-813a-b011ce13e860",
#       "comment": "",
#       "command": "click",
#       "target": "xpath=//div[6]/fieldset/rccr-currency-input/div/div/input",
#       "targets": [
#         ["id=69a60af2-fca1-4be2-2273-af4e649e19e3", "id"],
#         ["css=#\\\\36 9a60af2-fca1-4be2-2273-af4e649e19e3", "css:finder"],
#         ["xpath=//input[@id='69a60af2-fca1-4be2-2273-af4e649e19e3']", "xpath:attributes"],
#         ["xpath=//div[6]/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "b3e532b2-5649-4df2-bc52-9b9e94085b84",
#       "comment": "",
#       "command": "type",
#       "target": "xpath=//div[6]/fieldset/rccr-currency-input/div/div/input",
#       "targets": [
#         ["id=69a60af2-fca1-4be2-2273-af4e649e19e3", "id"],
#         ["css=#\\\\36 9a60af2-fca1-4be2-2273-af4e649e19e3", "css:finder"],
#         ["xpath=//input[@id='69a60af2-fca1-4be2-2273-af4e649e19e3']", "xpath:attributes"],
#         ["xpath=//div[6]/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     }''')
#     if True: # exempt pay
#         file.write(''',
# {
#       "id": "ca249722-67d1-466b-b012-968ab9b69bc0",
#       "comment": "",
#       "command": "click",
#       "target": "css=.ng-untouched:nth-child(13) label > span:nth-child(2)",
#       "targets": [
#         ["css=.ng-untouched:nth-child(13) label > span:nth-child(2)", "css:finder"],
#         ["xpath=//rccr-checkbox[7]/div/label/span", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "ec5c0721-dc99-4b0e-8571-51be705a15b3",
#       "comment": "",
#       "command": "click",
#       "target": "xpath=//div[7]/fieldset/rccr-currency-input/div/div/input",
#       "targets": [
#         ["id=f42d9122-a6dc-ea9f-31c1-c457f87ca396", "id"],
#         ["css=#f42d9122-a6dc-ea9f-31c1-c457f87ca396", "css:finder"],
#         ["xpath=//input[@id='f42d9122-a6dc-ea9f-31c1-c457f87ca396']", "xpath:attributes"],
#         ["xpath=//div[7]/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "d9c9880b-0ac7-4cd2-8b93-9ac9dde82af8",
#       "comment": "",
#       "command": "type",
#       "target": "xpath=//div[7]/fieldset/rccr-currency-input/div/div/input",
#       "targets": [
#         ["id=f42d9122-a6dc-ea9f-31c1-c457f87ca396", "id"],
#         ["css=#f42d9122-a6dc-ea9f-31c1-c457f87ca396", "css:finder"],
#         ["xpath=//input[@id='f42d9122-a6dc-ea9f-31c1-c457f87ca396']", "xpath:attributes"],
#         ["xpath=//div[7]/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "8c1e6a9e-68f9-4d36-868f-fcb9c81d2085",
#       "comment": "",
#       "command": "click",
#       "target": "xpath=//div[7]/fieldset/rccr-currency-input[2]/div/div/input",
#       "targets": [
#         ["id=ad9195e0-03b9-d4f0-22bb-d9a051e147bb", "id"],
#         ["css=#ad9195e0-03b9-d4f0-22bb-d9a051e147bb", "css:finder"],
#         ["xpath=//input[@id='ad9195e0-03b9-d4f0-22bb-d9a051e147bb']", "xpath:attributes"],
#         ["xpath=//div[7]/fieldset/rccr-currency-input[2]/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "7d4a8454-14ce-48e8-bbca-54027c21df27",
#       "comment": "",
#       "command": "type",
#       "target": "xpath=//div[7]/fieldset/rccr-currency-input[2]/div/div/input",
#       "targets": [
#         ["id=ad9195e0-03b9-d4f0-22bb-d9a051e147bb", "id"],
#         ["css=#ad9195e0-03b9-d4f0-22bb-d9a051e147bb", "css:finder"],
#         ["xpath=//input[@id='ad9195e0-03b9-d4f0-22bb-d9a051e147bb']", "xpath:attributes"],
#         ["xpath=//div[7]/fieldset/rccr-currency-input[2]/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     }''')
#     if True: # other annual deduction
#         file.write('''
# ,
# {
#       "id": "b3128671-4be9-40c4-b122-2cef8b2c8479",
#       "comment": "",
#       "command": "click",
#       "target": "css=.ng-untouched:nth-child(15) label > span:nth-child(2)",
#       "targets": [
#         ["css=.ng-untouched:nth-child(15) label > span:nth-child(2)", "css:finder"],
#         ["xpath=//rccr-checkbox[8]/div/label/span", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "f5543df9-b0dc-42bd-b280-9acd1451a01f",
#       "comment": "",
#       "command": "click",
#       "target": "xpath=//div[8]/fieldset/rccr-currency-input/div/div/input",
#       "targets": [
#         ["id=e99d973e-0743-6458-0c9f-5723e799fbfe", "id"],
#         ["css=#e99d973e-0743-6458-0c9f-5723e799fbfe", "css:finder"],
#         ["xpath=//input[@id='e99d973e-0743-6458-0c9f-5723e799fbfe']", "xpath:attributes"],
#         ["xpath=//div[8]/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "85073f16-b4df-4938-821a-45c9abe694b9",
#       "comment": "",
#       "command": "type",
#       "target": "xpath=//div[8]/fieldset/rccr-currency-input/div/div/input",
#       "targets": [
#         ["id=e99d973e-0743-6458-0c9f-5723e799fbfe", "id"],
#         ["css=#e99d973e-0743-6458-0c9f-5723e799fbfe", "css:finder"],
#         ["xpath=//input[@id='e99d973e-0743-6458-0c9f-5723e799fbfe']", "xpath:attributes"],
#         ["xpath=//div[8]/fieldset/rccr-currency-input/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "bf749a65-1cf2-4d9b-aed6-72110492cdeb",
#       "comment": "",
#       "command": "click",
#       "target": "xpath=//div[8]/fieldset/rccr-currency-input[2]/div/div/input",
#       "targets": [
#         ["id=cd24ea85-4587-b0d9-5ece-2be53c19b8de", "id"],
#         ["css=#cd24ea85-4587-b0d9-5ece-2be53c19b8de", "css:finder"],
#         ["xpath=//input[@id='cd24ea85-4587-b0d9-5ece-2be53c19b8de']", "xpath:attributes"],
#         ["xpath=//div[8]/fieldset/rccr-currency-input[2]/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "77ec517e-6401-42ca-9b83-d7d3d04a0a56",
#       "comment": "",
#       "command": "type",
#       "target": "xpath=//div[8]/fieldset/rccr-currency-input[2]/div/div/input",
#       "targets": [
#         ["id=cd24ea85-4587-b0d9-5ece-2be53c19b8de", "id"],
#         ["css=#cd24ea85-4587-b0d9-5ece-2be53c19b8de", "css:finder"],
#         ["xpath=//input[@id='cd24ea85-4587-b0d9-5ece-2be53c19b8de']", "xpath:attributes"],
#         ["xpath=//div[8]/fieldset/rccr-currency-input[2]/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "f18b0f55-fd46-4224-a1af-b62efdbd4063",
#       "comment": "",
#       "command": "click",
#       "target": "xpath=//div[8]/fieldset/rccr-currency-input[3]/div/div/input",
#       "targets": [
#         ["id=08a0050b-2ab8-4c27-2b6d-b135f0470ec4", "id"],
#         ["css=#\\\\30 8a0050b-2ab8-4c27-2b6d-b135f0470ec4", "css:finder"],
#         ["xpath=//input[@id='08a0050b-2ab8-4c27-2b6d-b135f0470ec4']", "xpath:attributes"],
#         ["xpath=//div[8]/fieldset/rccr-currency-input[3]/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     },
# {
#       "id": "2b11608b-c3cf-4c71-9f7b-d71d2bb8513c",
#       "comment": "",
#       "command": "type",
#       "target": "xpath=//div[8]/fieldset/rccr-currency-input[3]/div/div/input",
#       "targets": [
#         ["id=08a0050b-2ab8-4c27-2b6d-b135f0470ec4", "id"],
#         ["css=#\\\\30 8a0050b-2ab8-4c27-2b6d-b135f0470ec4", "css:finder"],
#         ["xpath=//input[@id='08a0050b-2ab8-4c27-2b6d-b135f0470ec4']", "xpath:attributes"],
#         ["xpath=//div[8]/fieldset/rccr-currency-input[3]/div/div/input", "xpath:position"]
#       ],
#       "value": ""
#     }        ''')

    # clean up
    # next page
    file.write('''
    , 	
{
      "id": "203457d9-2e3c-4802-a745-99508b53973d",
      "comment": "",
      "command": "click",
      "target": "css=.next",
      "targets": [
        ["css=.next", "css:finder"],
        ["xpath=//button", "xpath:position"],
        ["xpath=//button[contains(.,'Next')]", "xpath:innerText"]
      ],
      "value": ""
    }''')


def additional(file, detail):
    commands = []

    # commands.append(ScriptLib.command_target_value("click", "xpath=//div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//div/input", validate_value(detail['FED_PER_TAX_CRD'])))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//rccr-currency-input[2]/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//rccr-currency-input[2]/div/div/input", validate_value(detail['FED_ADD_TAX'])))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//rccr-currency-input[3]/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//rccr-currency-input[3]/div/div/input", validate_value(detail['ONT_PER_TAX_CRD'])))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//rccr-integer-input/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//rccr-integer-input/div/div/input", validate_value(detail['PEN_MON'], True)))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//div/fieldset/div/rccr-currency-input/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//div/fieldset/div/rccr-currency-input/div/div/input", validate_value(detail['C2_AG_YTD'])))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//div/fieldset/div/rccr-currency-input[2]/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//div/fieldset/div/rccr-currency-input[2]/div/div/input", validate_value(detail['CP_YTD'])))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//div/fieldset/div/rccr-currency-input[3]/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//div/fieldset/div/rccr-currency-input[3]/div/div/input", validate_value(detail['C2_YTD'])))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//rccr-button-group[2]/div/fieldset/div/rccr-currency-input/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//rccr-button-group[2]/div/fieldset/div/rccr-currency-input/div/div/input", validate_value(detail['EI_AG_YTD'])))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//rccr-button-group[2]/div/fieldset/div/rccr-currency-input[2]/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//rccr-button-group[2]/div/fieldset/div/rccr-currency-input[2]/div/div/input", validate_value(detail['EI_YTD'])))

    # commands.append(ScriptLib.command_target_value("click", "xpath=//rccr-text-input/div/div/input", ""))
    commands.append(ScriptLib.command_target_value("type", "xpath=//rccr-text-input/div/div/input", validate_value(detail['EI_EMPR_PC'], True)))

    commands.append(ScriptLib.command_target_value("click", "css=.btn-primary:nth-child(1)", ""))

    commands.append(ScriptLib.command_target_value("Output", "xpath=/html/body/app-root/rccr-wet-template/div/div/main/app-results/app-results-bonus/table", ""))

    file.write(',' + ','.join(commands))

def additional_old(file, detail):
    if detail['FED_PER_TAX_CRD'] is not None:
        file.write('''
, 	
{
      "id": "4f0726cb-27a4-4adc-8fbb-103d0e02391d",
      "comment": "",
      "command": "click",
      "target": "xpath=//div/input",
      "targets": [
        ["id=400165c1-ffac-86c4-5a43-6e9b5c2052b7", "id"],
        ["css=#\\\\34 00165c1-ffac-86c4-5a43-6e9b5c2052b7", "css:finder"],
        ["xpath=//input[@id='400165c1-ffac-86c4-5a43-6e9b5c2052b7']", "xpath:attributes"],
        ["xpath=//div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "f92f3730-1906-4460-b713-0d9c22d8721d",
      "comment": "",
      "command": "click",
      "target": "xpath=//div/input",
      "targets": [
        ["id=400165c1-ffac-86c4-5a43-6e9b5c2052b7", "id"],
        ["css=#\\\\34 00165c1-ffac-86c4-5a43-6e9b5c2052b7", "css:finder"],
        ["xpath=//input[@id='400165c1-ffac-86c4-5a43-6e9b5c2052b7']", "xpath:attributes"],
        ["xpath=//div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "54390b47-0cc0-4306-8b59-56aecb9bb08b",
      "comment": "",
      "command": "type",
      "target": "xpath=//div/input",
      "targets": [
        ["id=400165c1-ffac-86c4-5a43-6e9b5c2052b7", "id"],
        ["css=#\\\\34 00165c1-ffac-86c4-5a43-6e9b5c2052b7", "css:finder"],
        ["xpath=//input[@id='400165c1-ffac-86c4-5a43-6e9b5c2052b7']", "xpath:attributes"],
        ["xpath=//div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['FED_PER_TAX_CRD']) + '''"
    }        ''')
        if detail['FED_ADD_TAX'] is not None:
            file.write('''
    , 	
    {
          "id": "4f0726cb-27a4-4adc-8fbb-103d0e02391d",
          "comment": "",
          "command": "click",
          "target": "xpath=/html/body/app-root/rccr-wet-template/div/div/main/app-step3/form/fieldset[1]/div/rccr-currency-input[2]/div/div/input",
          "targets": [
            ["id=400165c1-ffac-86c4-5a43-6e9b5c2052b7", "id"],
            ["css=#\\\\34 00165c1-ffac-86c4-5a43-6e9b5c2052b7", "css:finder"],
            ["xpath=//input[@id='400165c1-ffac-86c4-5a43-6e9b5c2052b7']", "xpath:attributes"],
            ["xpath=/html/body/app-root/rccr-wet-template/div/div/main/app-step3/form/fieldset[1]/div/rccr-currency-input[2]/div/div/input", "xpath:position"]
          ],
          "value": ""
        }, 	
    {
          "id": "f92f3730-1906-4460-b713-0d9c22d8721d",
          "comment": "",
          "command": "click",
          "target": "xpath=/html/body/app-root/rccr-wet-template/div/div/main/app-step3/form/fieldset[1]/div/rccr-currency-input[2]/div/div/input",
          "targets": [
            ["id=400165c1-ffac-86c4-5a43-6e9b5c2052b7", "id"],
            ["css=#\\\\34 00165c1-ffac-86c4-5a43-6e9b5c2052b7", "css:finder"],
            ["xpath=//input[@id='400165c1-ffac-86c4-5a43-6e9b5c2052b7']", "xpath:attributes"],
            ["xpath=/html/body/app-root/rccr-wet-template/div/div/main/app-step3/form/fieldset[1]/div/rccr-currency-input[2]/div/div/input", "xpath:position"]
          ],
          "value": ""
        }, 	
    {
          "id": "54390b47-0cc0-4306-8b59-56aecb9bb08b",
          "comment": "",
          "command": "type",
          "target": "xpath=/html/body/app-root/rccr-wet-template/div/div/main/app-step3/form/fieldset[1]/div/rccr-currency-input[2]/div/div/input",
          "targets": [
            ["id=400165c1-ffac-86c4-5a43-6e9b5c2052b7", "id"],
            ["css=#\\\\34 00165c1-ffac-86c4-5a43-6e9b5c2052b7", "css:finder"],
            ["xpath=//input[@id='400165c1-ffac-86c4-5a43-6e9b5c2052b7']", "xpath:attributes"],
            ["xpath=/html/body/app-root/rccr-wet-template/div/div/main/app-step3/form/fieldset[1]/div/rccr-currency-input[2]/div/div/input", "xpath:position"]
          ],
          "value": "''' + validate_value(detail['FED_ADD_TAX']) + '''"
        }        ''')
    if detail['ONT_PER_TAX_CRD'] is not None:
        file.write('''
, 	
{
      "id": "010baf96-63f8-42c3-922c-98cc3da054e7",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-currency-input[3]/div/div/input",
      "targets": [
        ["id=e62c54d9-2262-052a-3cb8-1d3b4936c152", "id"],
        ["css=#e62c54d9-2262-052a-3cb8-1d3b4936c152", "css:finder"],
        ["xpath=//input[@id='e62c54d9-2262-052a-3cb8-1d3b4936c152']", "xpath:attributes"],
        ["xpath=//rccr-currency-input[3]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "fd139611-54ca-45c6-86d5-8db970ed1cfd",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-currency-input[3]/div/div/input",
      "targets": [
        ["id=e62c54d9-2262-052a-3cb8-1d3b4936c152", "id"],
        ["css=#e62c54d9-2262-052a-3cb8-1d3b4936c152", "css:finder"],
        ["xpath=//input[@id='e62c54d9-2262-052a-3cb8-1d3b4936c152']", "xpath:attributes"],
        ["xpath=//rccr-currency-input[3]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "9de3a95f-d247-4369-9d82-5dd91f9b287b",
      "comment": "",
      "command": "type",
      "target": "xpath=//rccr-currency-input[3]/div/div/input",
      "targets": [
        ["id=e62c54d9-2262-052a-3cb8-1d3b4936c152", "id"],
        ["css=#e62c54d9-2262-052a-3cb8-1d3b4936c152", "css:finder"],
        ["xpath=//input[@id='e62c54d9-2262-052a-3cb8-1d3b4936c152']", "xpath:attributes"],
        ["xpath=//rccr-currency-input[3]/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['ONT_PER_TAX_CRD']) + '''"
    }        ''')
    if detail['C2_AG_YTD'] is not None:
        file.write('''
, 	
{
      "id": "35e335ba-79e9-4d11-a622-a92b6fc84752",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-integer-input/div/div/input",
      "targets": [
        ["id=037b5a9f-7f2d-cca8-eb4f-4b85675afd59", "id"],
        ["css=#\\\\30 37b5a9f-7f2d-cca8-eb4f-4b85675afd59", "css:finder"],
        ["xpath=//input[@id='037b5a9f-7f2d-cca8-eb4f-4b85675afd59']", "xpath:attributes"],
        ["xpath=//rccr-integer-input/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "0e00f0d3-185d-4a8f-850d-9141abba7849",
      "comment": "",
      "command": "click",
      "target": "xpath=//div/fieldset/div/rccr-currency-input/div/div/input",
      "targets": [
        ["id=432436af-6af5-6e10-32f2-a78a6bbed6b7", "id"],
        ["css=#\\\\34 32436af-6af5-6e10-32f2-a78a6bbed6b7", "css:finder"],
        ["xpath=//input[@id='432436af-6af5-6e10-32f2-a78a6bbed6b7']", "xpath:attributes"],
        ["xpath=//div/fieldset/div/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "700e233f-1b54-4f96-b768-e8731281ce6e",
      "comment": "",
      "command": "type",
      "target": "xpath=//div/fieldset/div/rccr-currency-input/div/div/input",
      "targets": [
        ["id=432436af-6af5-6e10-32f2-a78a6bbed6b7", "id"],
        ["css=#\\\\34 32436af-6af5-6e10-32f2-a78a6bbed6b7", "css:finder"],
        ["xpath=//input[@id='432436af-6af5-6e10-32f2-a78a6bbed6b7']", "xpath:attributes"],
        ["xpath=//div/fieldset/div/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['C2_AG_YTD']) + '''"
    }       ''')
    if detail['CP_YTD'] is not None:
        file.write('''
        , 	
{
      "id": "77e7bf37-25d8-4da1-add2-d9e28c7ddabb",
      "comment": "",
      "command": "click",
      "target": "xpath=//div/fieldset/div/rccr-currency-input[2]/div/div/input",
      "targets": [
        ["id=ec43b6eb-1963-1f3e-70a9-dd6ab71ba8eb", "id"],
        ["css=#ec43b6eb-1963-1f3e-70a9-dd6ab71ba8eb", "css:finder"],
        ["xpath=//input[@id='ec43b6eb-1963-1f3e-70a9-dd6ab71ba8eb']", "xpath:attributes"],
        ["xpath=//div/fieldset/div/rccr-currency-input[2]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "1f9a349f-3904-4467-b062-1ddac5558ebc",
      "comment": "",
      "command": "type",
      "target": "xpath=//div/fieldset/div/rccr-currency-input[2]/div/div/input",
      "targets": [
        ["id=ec43b6eb-1963-1f3e-70a9-dd6ab71ba8eb", "id"],
        ["css=#ec43b6eb-1963-1f3e-70a9-dd6ab71ba8eb", "css:finder"],
        ["xpath=//input[@id='ec43b6eb-1963-1f3e-70a9-dd6ab71ba8eb']", "xpath:attributes"],
        ["xpath=//div/fieldset/div/rccr-currency-input[2]/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['CP_YTD']) + '''"
    }''')
    if detail['C2_YTD'] is not None:
        file.write('''
, 	
{
      "id": "78c14d2c-47ee-4743-8d98-fb79219a8245",
      "comment": "",
      "command": "click",
      "target": "xpath=//div/fieldset/div/rccr-currency-input[3]/div/div/input",
      "targets": [
        ["id=7f12f45a-780b-e511-6e7b-88401d98e475", "id"],
        ["css=#\\\\37 f12f45a-780b-e511-6e7b-88401d98e475", "css:finder"],
        ["xpath=//input[@id='7f12f45a-780b-e511-6e7b-88401d98e475']", "xpath:attributes"],
        ["xpath=//div/fieldset/div/rccr-currency-input[3]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "f0062aa3-2c77-4314-b76b-571cf96f9b2e",
      "comment": "",
      "command": "type",
      "target": "xpath=//div/fieldset/div/rccr-currency-input[3]/div/div/input",
      "targets": [
        ["id=7f12f45a-780b-e511-6e7b-88401d98e475", "id"],
        ["css=#\\\\37 f12f45a-780b-e511-6e7b-88401d98e475", "css:finder"],
        ["xpath=//input[@id='7f12f45a-780b-e511-6e7b-88401d98e475']", "xpath:attributes"],
        ["xpath=//div/fieldset/div/rccr-currency-input[3]/div/div/input", "xpath:position"]
      ],
      "value": "'''+ validate_value(detail['C2_YTD']) +'''"
    }        ''')
    if detail['EI_AG_YTD'] is not None:
        file.write('''
        , 	
{
      "id": "3a860418-1196-44db-b706-af413fba6d63",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-button-group[2]/div/fieldset/div/rccr-currency-input/div/div/input",
      "targets": [
        ["id=dc33641e-9499-1134-8518-600506658c0d", "id"],
        ["css=#dc33641e-9499-1134-8518-600506658c0d", "css:finder"],
        ["xpath=//input[@id='dc33641e-9499-1134-8518-600506658c0d']", "xpath:attributes"],
        ["xpath=//rccr-button-group[2]/div/fieldset/div/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "3c2a3cee-cd5c-4e8c-9acc-8c5e48ac9446",
      "comment": "",
      "command": "type",
      "target": "xpath=//rccr-button-group[2]/div/fieldset/div/rccr-currency-input/div/div/input",
      "targets": [
        ["id=dc33641e-9499-1134-8518-600506658c0d", "id"],
        ["css=#dc33641e-9499-1134-8518-600506658c0d", "css:finder"],
        ["xpath=//input[@id='dc33641e-9499-1134-8518-600506658c0d']", "xpath:attributes"],
        ["xpath=//rccr-button-group[2]/div/fieldset/div/rccr-currency-input/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['EI_AG_YTD']) + '''"
    }
, 	
{
      "id": "071aa1a5-03b5-4631-b29b-25bee3b05c9c",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-button-group[2]/div/fieldset/div/rccr-currency-input[2]/div/div/input",
      "targets": [
        ["id=2791334f-3c4d-2fa6-68ff-2f2c2a1f18ad", "id"],
        ["css=#\\\\32 791334f-3c4d-2fa6-68ff-2f2c2a1f18ad", "css:finder"],
        ["xpath=//input[@id='2791334f-3c4d-2fa6-68ff-2f2c2a1f18ad']", "xpath:attributes"],
        ["xpath=//rccr-button-group[2]/div/fieldset/div/rccr-currency-input[2]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "e05bb7df-d230-4ffd-9796-7ad8e3ab4e17",
      "comment": "",
      "command": "type",
      "target": "xpath=//rccr-button-group[2]/div/fieldset/div/rccr-currency-input[2]/div/div/input",
      "targets": [
        ["id=2791334f-3c4d-2fa6-68ff-2f2c2a1f18ad", "id"],
        ["css=#\\\\32 791334f-3c4d-2fa6-68ff-2f2c2a1f18ad", "css:finder"],
        ["xpath=//input[@id='2791334f-3c4d-2fa6-68ff-2f2c2a1f18ad']", "xpath:attributes"],
        ["xpath=//rccr-button-group[2]/div/fieldset/div/rccr-currency-input[2]/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['EI_YTD']) + '''"
    }''')

    file.write(''', {
      "id": "0366c37d-b2d4-493d-a66c-a4cf1cbfb7f6",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-text-input/div/div/input",
      "targets": [
        ["id=336542e6-2271-5f77-5ed8-e01c6907ceb6", "id"],
        ["css=#\\\\33 36542e6-2271-5f77-5ed8-e01c6907ceb6", "css:finder"],
        ["xpath=//input[@id='336542e6-2271-5f77-5ed8-e01c6907ceb6']", "xpath:attributes"],
        ["xpath=//rccr-text-input/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "3b491741-fc8f-487d-b089-693a2647db7b",
      "comment": "",
      "command": "type",
      "target": "xpath=//rccr-text-input/div/div/input",
      "targets": [
        ["id=336542e6-2271-5f77-5ed8-e01c6907ceb6", "id"],
        ["css=#\\\\33 36542e6-2271-5f77-5ed8-e01c6907ceb6", "css:finder"],
        ["xpath=//input[@id='336542e6-2271-5f77-5ed8-e01c6907ceb6']", "xpath:attributes"],
        ["xpath=//rccr-text-input/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['EI_EMPR_PC'], True) + '''"
    }
''')

    # Month
    file.write('''
,    {
      "id": "17a896d8-d72f-4959-b48e-b14e106a27f5",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-integer-input/div/div/input",
      "targets": [
        ["id=b2404c10-14a6-02c3-d22c-36cd9aebfc1d", "id"],
        ["css=#b2404c10-14a6-02c3-d22c-36cd9aebfc1d", "css:finder"],
        ["xpath=//input[@id='b2404c10-14a6-02c3-d22c-36cd9aebfc1d']", "xpath:attributes"],
        ["xpath=//rccr-integer-input/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "80897d99-0550-4afd-ad45-2fb988c69f78",
      "comment": "",
      "command": "type",
      "target": "xpath=//rccr-integer-input/div/div/input",
      "targets": [
        ["id=b2404c10-14a6-02c3-d22c-36cd9aebfc1d", "id"],
        ["css=#b2404c10-14a6-02c3-d22c-36cd9aebfc1d", "css:finder"],
        ["xpath=//input[@id='b2404c10-14a6-02c3-d22c-36cd9aebfc1d']", "xpath:attributes"],
        ["xpath=//rccr-integer-input/div/div/input", "xpath:position"]
      ],
      "value": "''' + validate_value(detail['PEN_MON'], True) + '''"
    }''')

    file.write('''
    , 	
{
      "id": "bcbc20ab-82d8-4c25-a639-75b05e0c0b1a",
      "comment": "",
      "command": "click",
      "target": "xpath=//rccr-text-input/div/div/input",
      "targets": [
        ["id=d5612a5d-f239-aa03-25d4-d3255f53b5b7", "id"],
        ["css=#d5612a5d-f239-aa03-25d4-d3255f53b5b7", "css:finder"],
        ["xpath=//input[@id='d5612a5d-f239-aa03-25d4-d3255f53b5b7']", "xpath:attributes"],
        ["xpath=//rccr-text-input/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, 	
{
      "id": "e41594c7-4c3b-44cc-b221-b2b1b0a3db95",
      "comment": "",
      "command": "click",
      "target": "css=.btn-primary:nth-child(1)",
      "targets": [
        ["css=.btn-primary:nth-child(1)", "css:finder"],
        ["xpath=//button", "xpath:position"],
        ["xpath=//button[contains(.,'Calculate')]", "xpath:innerText"]
      ],
      "value": ""
    }''')

    # Calculation results, the last page
    file.write('''
    , 	
{
      "id": "27786e07-a83d-42f6-9fe8-962eec693052",
      "comment": "",
      "command": "Output",
      "target": "xpath=/html/body/app-root/rccr-wet-template/div/div/main/app-results/app-results-bonus/table",
      "targets": [
        ["id=cec15b8b-a57a-6f9a-9f12-1861ba6680c4", "id"],
        ["css=#cec15b8b-a57a-6f9a-9f12-1861ba6680c4", "css:finder"],
        ["xpath=//input[@id='cec15b8b-a57a-6f9a-9f12-1861ba6680c4']", "xpath:attributes"],
        ["xpath=//fieldset/rccr-currency-input[3]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }''')

def convert_row_to_script(detail):
    script_name = str(detail['SPRIDEN_ID']) + '.side'
    with open(script_name, 'w') as file:
        # init
        file.write('{\n  "id": "b4098ff3-655d-4b7d-9181-db93667eac24",\n  "version": "2.0",\n  "name": "PDOC",\n  "url": "https://apps.cra-arc.gc.ca",\n  "tests": [{\n    "id": "0bfa0854-377b-4513-b136-e268d0324bf1",\n    "name": "PDOC",\n    "commands": [')

        # 1st page
        preload(file)

        # 2nd page
        incomes(file, detail)

        # 3rd page
        additional(file, detail)
        # ending
        file.write(']\n  }],\n  "suites": [{\n    "id": "e5717ad0-6756-4b4e-8ae9-7d53ef765f81",\n    "name": "Default Suite",\n    "persistSession": false,\n    "parallel": false,\n    "timeout": 300,\n    "tests": ["0bfa0854-377b-4513-b136-e268d0324bf1"]\n  }],\n  "urls": ["https://apps.cra-arc.gc.ca/"],\n  "plugins": []\n}')

    return script_name