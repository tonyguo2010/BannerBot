import os
import FormBase
import JsonParser
operations = JsonParser.loadJsonFromFile('operations_' + os.path.basename(__file__).replace('.py', '').upper() + '.json')

widgets = {
    "Position Class" : {"id": "inp:key_block_pclsCode", "xpath": "/html/body/div/div/div[2]/div/div/form/div/div/div/div/div/div/input"},
    "Go" : {"id": "frames7", "xpath": "/html/body/div/div/div[2]/div/div/form/div[2]/button"},

    "Code" : {"id": "#frames18", "xpath": "/html/body/div/div/div[2]/div/div/form/div[3]/div/div/div[2]/div/div/div/div[2]/div/div/div[4]/div[3]/div/div/div/div/input"}
}

def handle(driver):
    FormBase.handle(driver, widgets, operations)
