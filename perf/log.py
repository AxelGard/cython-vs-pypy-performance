import json

def write_file(entry, file="./results.json"):
    with open(file=file, mode='w') as feedsjson:
        json.dump(entry, feedsjson)


def read_file(file="./results.json"):
    data = {}
    with open(file) as json_file:
        data = json.load(json_file)
    return data
