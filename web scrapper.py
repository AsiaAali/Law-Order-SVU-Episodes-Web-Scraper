import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    "https://en.wikipedia.org/wiki/List_of_Law_%26_Order:_Special_Victims_Unit_episodes_(seasons_1%E2%80%9319)",
    "https://en.wikipedia.org/wiki/List_of_Law_%26_Order:_Special_Victims_Unit_episodes_(seasons_20%E2%80%93present)"
]

# List to hold all titles
titles = []

# Loop through each URL
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully retrieved the page: {url}")
        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all episode titles in each table
        tables = soup.find_all('table', class_='wikitable plainrowheaders wikiepisodetable')
        for table in tables:
            for row in table.find_all('tr'):
                # Check for titles in <i> tags first
                title_cell = row.find(class_='summary')
                if title_cell:
                    title = title_cell.get_text(strip=True).replace('"', '').lower()  # Remove quotes
                    titles.append(title)
    else:
        print(f"Failed to retrieve the page: {url}")

# Write all titles to a text file
with open("svu_titles.txt", "w") as file:
    for title in titles:
        file.write(title + "\n")
print("All titles have been saved to svu_titles.txt without quotation marks.")
