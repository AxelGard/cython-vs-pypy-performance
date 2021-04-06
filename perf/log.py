import json

def write_file(entry, file="./results.json"):
    with open(file=file, mode='w', encoding='utf-8') as feedsjson:
        feeds.append(entry)
        json.dump(feeds, feedsjson)

