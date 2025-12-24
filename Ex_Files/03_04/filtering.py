import csv
import json
from pprint import pprint

with open("laureates2.csv", "r") as f:
    reader = csv.DictReader(f)
    All_laureates = list(reader)

laureates_beginning_with_a = []
laureatesWithCompton = []

for person in All_laureates:
    if person["name"].startswith("A"):
        laureates_beginning_with_a.append(person)

pprint(f"All laureates: {len(All_laureates)}")
pprint(f"Laureates with A: {len(laureates_beginning_with_a)}")
pprint("------------------------------")

for people in All_laureates:
    if people["surname"] == "Compton":
        laureatesWithCompton.append(people)
        pprint(people)

pprint(f"Comptons: {len(laureatesWithCompton)}")
