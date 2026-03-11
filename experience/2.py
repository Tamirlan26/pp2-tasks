import json
b={
    "totalCount": "5",
    "countries": [
        {
            "countryInfo": {
                "attributes": {
                    "name": "France",
                    "capital": "Paris",
                    "population": 67000000,
                    "continent": "Europe"
                }
            }
        },
        {
            "countryInfo": {
                "attributes": {
                    "name": "Japan",
                    "capital": "Tokyo",
                    "population": 125000000,
                    "continent": "Asia"
                }
            }
        },
        {
            "countryInfo": {
                "attributes": {
                    "name": "Brazil",
                    "capital": "Brasília",
                    "population": 211000000,
                    "continent": "South America"
                }
            }
        },
        {
            "countryInfo": {
                "attributes": {
                    "name": "Canada",
                    "capital": "Ottawa",
                    "population": 37590000,
                    "continent": "North America"
                }
            }
        },
        {
            "countryInfo": {
                "attributes": {
                    "name": "Australia",
                    "capital": "Canberra",
                    "population": 25690000,
                    "continent": "Oceania"
                }
            }
        }
    ]
}
#first_country = b["countries"][0]["countryInfo"]["attributes"]
#print(first_country)

#print(b["countries"][0]["countryInfo"]["attributes"]["name"])

#for country in b["countries"]:
#    attrs = country["countryInfo"]["attributes"]
#    print(attrs["name"], "-", attrs["continent"])

#for i in b["countries"]:
#    del i["countryInfo"]["attributes"]["population"]
#new=json.dumps(b,indent=2)
#print(new)

print("Data")
print("-"*86)
print(f"{"Name":<60} {"Capital":<10} {"Population":<6}")
print("-"*86)
for i in b["countries"]:
    c=i["countryInfo"]["attributes"]
    print(f"{c["name"]:<60} {c["capital"]:<10} {c["population"]:<6}")