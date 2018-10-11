#
# gets all builds for all heroes (prints or writes to file (json?) -> JSON!
from utils import get_soup, normalize_hero_name
from scrapping import get_hero_builds, print_build
import json
import requests
from bs4 import BeautifulSoup


'''
Automatically scrape the list of heroes from icy-veins and
write it to a json file (heroes.json)
'''
def update_heroes_list():
    heroes_names = set()
    roles = ['assassin', 'support', 'warrior', 'specialist']

    for role in roles:
        link = 'https://www.icy-veins.com/heroes/' + role + '-hero-guides'
        soup = get_soup(link)

        hero_block_tags = soup.find_all('div', class_='nav_content_block_entry_heroes_hero')
        for hero_block in hero_block_tags:
            name = normalize_hero_name(hero_block.find('span', class_='').contents[0])
            heroes_names.add(name)

    with open('data/heroes.json', 'w') as fp:
        json.dump(list(heroes_names), fp)


'''
Updates list of builds (in [hero name].json) for a given hero
'''
def update_hero_builds(hero):
    hero = normalize_hero_name(hero)
    print('Updating builds for ' + hero + '...', end='')
    builds, titles = get_hero_builds(hero)
    filename = 'data/builds/' + hero + '.json'

    with open(filename, 'w') as fp:
        for build, title in zip(builds, titles):
            json.dump(build, fp)
            json.dump(title, fp)

    print('OK')


'''
Updates all builds of all heroes (calls update_builds for all heroes)
'''
def update_all_builds():
    print('Starting full heroes build update')
    with open('data/heroes.json', 'r') as fp:
        heroes = json.load(fp)

    for hero in heroes:
        update_hero_builds(hero)


'''
Loads builds for one hero
'''
def load_builds(hero):
    hero = normalize_hero_name(hero)
    filename = 'data/builds/' + hero + '.json'

    with open(filename, 'r') as fp:
        data = json.load(fp)

    print(data)



def print_all_builds():
    with open('data/heroes.json', 'r') as fp:
        heroes = json.load(fp)

    with open('data/levels.json', 'r') as fp:
        levels = json.load(fp)

    for hero in heroes:
        print('-------------------------------- ' + hero + ' --------------------------------')
        builds, titles = load_builds(hero)
        for build, title in zip(builds, titles):
            print_build(levels, build, title)

update_all_builds()
