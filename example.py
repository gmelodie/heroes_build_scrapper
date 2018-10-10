
# Connects with iana.org/domains/reserved and gets links in a column

import requests
from bs4 import BeautifulSoup

page_url = 'https://www.iana.org/domains/reserved'

# Download page (is this only html?)
print('Getting page...')
page = requests.get(page_url)

if(page.status_code != 200):
    print('[' + str(page.status_code) + '] Failed when getting the page')
    exit(1)


soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find_all('tbody')
domains = soup.find_all('span', class_='domain label')
links = []

for domain in domains:
    if domain.find('a'):
        links.append(domain.find('a')['href'])

print(links)
