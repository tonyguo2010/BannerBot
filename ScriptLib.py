
def command_target_value(command : str, target : str, value : str):
    return '''
    {
      "id": "07def488-cc1d-4f55-8fa6-616772de7a70",
      "comment": "",
      "command": "''' + command + '''",
      "target": "''' + target + '''",
      "targets": [],
      "value": "''' + value + '''"
    } 	
    '''