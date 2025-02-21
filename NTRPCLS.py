import os
import FormBase
import JsonParser
operations = JsonParser.loadJsonFromFile('operations_' + os.path.basename(__file__).replace('.py', '').upper() + '.json')

widgets = {
    "Position Class Code":{"id": "inp:key_block_pclsCode", "xpath": "/html/body/div/div/div[2]/div/div/form/div/div/div/div/div/div/input"},
    "Go":{"id": "frames5", "xpath": "/html/body/div/div/div[2]/div/div/form/div[2]/button"},

    "Title": {"id": "inp:ntrpcls_ntrpclsDesc",
              "xpath": "/html/body/div[1]/div/div[2]/div/div/form/div[3]/div/div/div[2]/div/div/div/div[2]/fieldset[1]/div/table/tbody/tr[1]/td[1]/div/input"}

}

def handle(driver):
    FormBase.handle(driver, widgets, operations)
