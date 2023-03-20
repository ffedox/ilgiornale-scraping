import requests
from bs4 import BeautifulSoup

url = "https://www.ilgiornale.it/news/politica/tutele-esistono-gi-norma-non-ha-senso-ben-160-paesi-nel-1409848.html"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Extracting the required data
first_author = soup.find('div', class_='ga4-datalayer-events').get('data-ga4-event-first-author')
publication_date = soup.find('div', class_='ga4-datalayer-events').get('data-ga4-event-publication-date')
content = soup.find('div', class_='content__body typography').get_text(strip=True)

# Printing the extracted data
print("First Author: ", first_author)
print("Publication Date: ", publication_date)
print("Content: ", content)