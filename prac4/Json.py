import json

with open("experience/sample-data.json", "r", encoding="utf-8") as f:
    data = json.load(f)


print("Interface Status")
print("="*86)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-"*86)

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    print(f"{attrs['dn']:<50} {attrs['descr']:<20} {attrs['speed']:<6} {attrs['mtu']:<6}")
