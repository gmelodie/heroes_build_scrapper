
# Scrapes alextraza's build (has 2 builds)

import requests
from bs4 import BeautifulSoup

levels = [1, 4, 7, 10, 13, 16, 20] # levels in which one gets talents
page_link = 'https://www.icy-veins.com/heroes/alexstrasza-build-guide'

page = requests.get(page_link)
soup = BeautifulSoup(page.content, 'html.parser')

builds = soup.find_all('div', class_='heroes_tldr_talents')
build_title_tags = soup.find_all('h4', class_='toc_no_parsing')
build_titles = [title.get_text() for title in build_title_tags]

for build_number, build in enumerate(builds):
    print('============== ' + str(build_titles[build_number]) + ' ==============')
    talent_tiers = build.find_all('span', class_= 'heroes_tldr_talent_tier_visual')

    for level, tier in zip(levels, talent_tiers):
        print('Level ' + str(level), end=' ')
        children = tier.find_all('span')
        for j, child in enumerate(children):
            if('heroes_tldr_talent_tier_yes' in child['class']):
                print('Talent ' + str(j + 1))

