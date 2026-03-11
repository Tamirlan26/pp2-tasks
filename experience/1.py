import json

with open("experience/sample-data.json", "r", encoding="utf-8") as f:
    data = json.load(f)


print(type(data["imdata"]))
