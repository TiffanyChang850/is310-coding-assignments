import cloudscraper
from bs4 import BeautifulSoup
import json
import os

url = "https://onepiece.fandom.com/wiki/Roronoa_Zoro"
scrape = cloudscraper.create_scraper()
response = scrape.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
abilities = []
asec = soup.find("span", {"id": "Abilities_and_Powers"})
if asec:
  header = asec.find_parent(["h2", "h3"])
  for s in header.find_next_siblings():
        if sibling.name in ["h2", "h3"]:
            break
  for li in sibling.find_all("li"):
            text = li.get_text(strip=True)
            if text:
                abilities_data.append(text)
os.makedirs("webscrape", exist_ok = True)
output_file = "web_scraping_assignments/zoro_abilities.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(abilities_data, f, indent=4, ensure_ascii=False)

print(f"Saved {len(abilities_data)} abilities to {output_file}")
