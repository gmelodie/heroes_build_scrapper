
# Scrapes uther's build (this is easy because uther has only 1 build)

import requests
from bs4 import BeautifulSoup

levels = [1, 4, 7, 10, 13, 16, 20] # levels in which one gets talents
page_link = 'https://www.icy-veins.com/heroes/uther-build-guide'

page = requests.get(page_link)
soup = BeautifulSoup(page.content, 'html.parser')

talent_tiers = soup.find_all('span', class_= 'heroes_tldr_talent_tier_visual')

for level, tier in zip(levels, talent_tiers):
    print('Level ' + str(level), end=' ')
    children = tier.find_all('span')
    for j, child in enumerate(children):
        if('heroes_tldr_talent_tier_yes' in child['class']):
            print('Talent ' + str(j + 1))

