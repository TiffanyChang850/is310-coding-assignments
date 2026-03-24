import cloudscraper
import pandas as pd
from bs4 import BeautifulSoup

url = "https://onepiece.fandom.com/wiki/Roronoa_Zoro"

scraper = cloudscraper.create_scraper()
response = scraper.get(url)
soup = BeautifulSoup(response.text, "html.parser")

abilities = []

section_header = soup.find(["h2", "h3"], string=lambda s: s and ("Abilities" in s or "Powers" in s))

if section_header:
    print(f"Found section: {section_header.name} - {section_header.get_text(strip=True)}")
    
    for tag in section_header.find_next_siblings():
        if tag.name in ["h2", "h3"]:
            break
        
        if tag.name == "p":
            text = tag.get_text(strip=True)
            if text and len(text) > 10:
                abilities.append(text)
        
        if tag.name == "ul":
            for li in tag.find_all("li"):
                text = li.get_text(strip=True)
                if text:
                    abilities.append(text)

if not abilities:
    abilities_section = soup.find("div", class_="mw-parser-output")
    if abilities_section:
        for tag in abilities_section.find_all(["p", "li"]):
            text = tag.get_text(strip=True)
            if text and ("sword" in text.lower() or "technique" in text.lower() or "style" in text.lower()):
                abilities.append(text)

df = pd.DataFrame(abilities, columns=["Abilities"])
df.to_csv("fandomscrape.csv", index=False)

print(f"Saved {len(abilities)} entries")
