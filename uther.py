
# Scrapes uther's build (this is easy because uther has only 1 build)

import requests
from bs4 import BeautifulSoup

page_link = 'https://www.icy-veins.com/heroes/uther-build-guide'

page = requests.get(page_link)
soup = BeautifulSoup(page.content, 'html.parser')

talent_tiers = soup.find_all('span', class_= 'heroes_tldr_talent_tier_visual')

for i, tier in enumerate(talent_tiers):
    print('Talent ' + str(i + 1))
    for j, child in enumerate(tier.children):
        print(child)
    #no_talents = tier.find_all('span', class_= 'heroes_tldr_talent_tier_no')
    #sit_talents = tier.find_all('span', class_= 'heroes_tldr_talent_tier_situational')
    #yes_talents = tier.find_all('span', class_= 'heroes_tldr_talent_tier_yes')
