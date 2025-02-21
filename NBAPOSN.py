import os
import FormBase
import JsonParser
operations = JsonParser.loadJsonFromFile('operations_' + os.path.basename(__file__).replace('.py', '').upper() + '.json')

widgets = {
    "Position Number" : {"id": "inp:key_block_key_block_posn", "xpath": "/html/body/div/div/div[2]/div/div/form/div/div/div/div/div/input"},
    "Go" : {"id": "frames4", "xpath": "/html/body/div/div/div[2]/div/div/form/div[2]/button"},

    "Position Class" : {"id": "inp:nbbposn_nbbposn_nbbposnPclsCode", "xpath": "/html/body/div/div/div[2]/div/div/form/div[3]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td/div/div/input"}
}

def handle(driver):
    FormBase.handle(driver, widgets, operations)
