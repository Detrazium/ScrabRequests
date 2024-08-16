import requests
from bs4 import BeautifulSoup

all_urls = 'https://norelem.de/sitemap/en-de.xml'

responce = requests.get(all_urls)
soup = BeautifulSoup(responce.text, 'html.parser')
urls = soup.select('loc')
with open('all_urls.txt', 'w', encoding='utf=8') as file:
    for i in urls:
        file.write(i.text + '\n')

