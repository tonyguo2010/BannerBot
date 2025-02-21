import os
import FormBase
import JsonParser
operations = JsonParser.loadJsonFromFile('operations_' + os.path.basename(__file__).replace('.py', '').upper() + '.json')

widgets = {
    "PendingChange": {"id": "inp:key_block_pendingChanges_btn",
                      "xpath": "/html/body/div/div/div[2]/div/div/form/div/div/div/div/div/div/button"},
    "ProxyFor": {"id": "inp:key_block_proxyForUserId",
                 "xpath": "/html/body/div/div/div[2]/div/div/form/div/div/div/div[2]/div/div/input"},
    "ID": {"id": "inp:key_block_id",
           "xpath": "/html/body/div/div/div[2]/div/div/form/div/div/div[2]/div/div/div/input"},
    "Transaction": {"id": "inp:key_block_transNo",
                    "xpath": "/html/body/div/div/div[2]/div/div/form/div/div/div[2]/div[2]/div/div/input"},
    "QueryDate": {"id": "pnlNortran1Canvas_effectiveDate1737603549513",
                  "xpath": "/html/body/div/div/div[2]/div/div/form/div/div/div[3]/div/div/input"},
    "LastPaidDate": {"id": "pnlNortran1Canvas_lastPaidDate1737603549516",
                     "xpath": "/html/body/div/div/div[2]/div/div/form/div/div/div[3]/div[2]/div/input"},
    "ApprovalCategory": {"id": "inp:key_block_acatCode",
                         "xpath": "/html/body/div/div/div[2]/div/div/form/div/div/div[4]/div/div/div/input"},
    "ApprovalType": {"id": "inp:key_block_aptyCode",
                     "xpath": "/html/body/div/div/div[2]/div/div/form/div/div/div[4]/div[2]/div/div/input"},
    "Position": {"id": "inp:key_block_posn",
                 "xpath": "/html/body/div/div/div[2]/div/div/form/div/div/div[5]/div/div/div/input"},
    "Suffix": {"id": "inp:key_block_suffix",
               "xpath": "/html/body/div/div/div[2]/div/div/form/div/div/div[5]/div[2]/div/div/input"},
    "Go": {"id": "frames20", "xpath": "/html/body/div/div/div[2]/div/div/form/div[2]/button"}

}

def handle(driver):
    FormBase.handle(driver, widgets, operations)
