import json

def loadJsonFromFile(file_name):
    with open(file_name, mode="r", encoding="utf-8") as read_file:
        content = json.load(read_file)
        return content

    return '{}'

def loadScriptFromJson(file_name):
    with open(file_name, mode="r", encoding="utf-8") as read_file:
        content = json.load(read_file)
        steps = content['tests'][0]
        return steps

    return '{}'

def loadBaseUrl(file_name):
    j_content = loadJsonFromFile(file_name)
    base_url = j_content['url']
    return base_url
#
# content = loadScriptFromJson("PCL.json")
# steps = content['tests'][0]['commands']
# for step in steps:
#     print(step['command'])
#     print(step['target'])
#     print(step['value'])
