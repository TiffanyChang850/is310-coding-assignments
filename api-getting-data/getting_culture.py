import requests
import json
from rich import print

SWAPI_URL = "https://swapi.dev/api/people/1/"
EUROPEANA_KEY = "****use your own api key"
EUROPEANA_URL = "https://api.europeana.eu/record/v2/search.json"

swapi_response = requests.get(SWAPI_URL)
swapi_data = swapi_response.json()

print("[bold yellow]SWAPI DATA[/bold yellow]")
print(swapi_data)

name = swapi_data["name"]

params = {
    "query": name,
    "wskey": EUROPEANA_KEY,
    "rows": 1
}

europeana_response = requests.get(EUROPEANA_URL, params=params)
europeana_data = europeana_response.json()

print("\n[bold cyan]EUROPEANA DATA[/bold cyan]")
print(europeana_data)

item = {
    "swapi": {
        "name": swapi_data["name"],
        "height": swapi_data["height"],
        "mass": swapi_data["mass"],
        "birth_year": swapi_data["birth_year"]
    },
    "europeana": europeana_data.get("items", [])
}

with open("swapi_europeana.json", "w") as f:
    json.dump(item, f, indent=2)

print("\nSaved to swapi_europeana.json")
