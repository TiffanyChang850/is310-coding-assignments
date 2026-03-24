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
                abilities.append(text)

df = pd.DataFrame(abilities)
df.to_csv('fandomscrape.csv', index=False)
