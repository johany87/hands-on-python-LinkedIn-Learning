import requests
import pprint as pprint

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json",
)

last_twenty_years = response.json()[1][:5]
#print(last_twenty_years)
for year in last_twenty_years:
    barwidth = "=" * (year['value'] // 10_000_000)
    pprint.pprint(f"Year: {year['date']} - habitants:{year['value']} - {barwidth}") 

