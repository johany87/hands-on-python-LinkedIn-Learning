import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json)
#print(einstein_json)
#pprint(back_to_dict)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


# 1. you can access parts of strings the same way you do lists
#      hey[2] == "y"
# 2. You can add to a list using
#      my_list.append("something")

laureates_beginning_with_a = []
laureatesWithCompton = []
# LinkedIn learner code here
for person in laureates:
    if person["name"].startswith("A"):
        laureates_beginning_with_a.append(person)

comptons = [person for person in laureates if person["surname"] == "Compton"]
for person in comptons:
    pprint(person)

pprint(f"Length: {len(laureatesWithCompton)}")
#pprint(laureatesWithCompton)

#laureates_beginning_with_a[0]["extra"] = "Navarro"
#pprint(laureates_beginning_with_a)
pprint("===========================")
with open("laureatesA.json", "w") as f:
    json.dump(laureates_beginning_with_a, f, indent=2)
    #pprint(f"Laureates total: {len(laureates)}")
    #pprint(f"Laureates with A: {len(laureates_beginning_with_a)}")
