#
# gets all builds for all heroes (prints or writes to file (json?)
from multiple import get_builds, print_build
import json
import requests
from bs4 import BeautifulSoup


def get_soup(link):
    page = requests.get(link)
    return BeautifulSoup(page.content, 'html.parser')


'''
Automatically scrape the list of heroes from icy-veins and
write it to a json file (heroes.json)
'''
def update_heroes_list():
    heroes_names = []
    roles = ['assassin', 'support', 'warrior', 'specialist']

    for role in roles:
        link = 'https://www.icy-veins.com/heroes/' + role + '-hero-guides'
        soup = get_soup(link)
        hero_block_tags = soup.find_all('div', class_='nav_content_block_entry_heroes_hero')
        print(hero_block_tags)
        hero_names = [hero.find('span', class_='').get_txt() for hero in list(hero_block_tags)]

        #heroes_names += [hero_tag.get_txt() for hero_tag in heroes_tags]
        #[print(hero_tag.get_txt()) for hero_tag in heroes_tags]

    with open('data/heroes.json', 'w') as fp:
        json.dump(heroes_names)


'''
Updates list of builds (in [hero name].json) for a given hero
'''
def update_builds(hero):
    pass


'''
Updates all builds of all heroes (calls update_builds for all heroes)
'''
def update_all_builds():
    pass


def print_all_builds():
    with open('data/heroes.json', 'r') as fp:
        heroes = json.load(fp)

    for hero in heroes:
        print('-------------------------------- ' + hero + ' --------------------------------')
        builds, titles = get_builds(hero)
        for build, title in zip(builds, titles):
            print_build(levels, build, title)

update_heroes_list()
