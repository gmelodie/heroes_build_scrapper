# Utilities' library

import json
import unicodedata
import requests
from bs4 import BeautifulSoup


def get_soup(link):
    '''Gets a link, downloads page and gets soup
    Returns beautifulsoup object
    '''
    page = requests.get(link)
    return BeautifulSoup(page.content, 'html.parser')


def get_heroes_list():
    with open('data/heroes.json', 'r') as fp:
        heroes = json.load(fp)

    return sorted(heroes)


def print_build(build, title):
    string = ''

    with open('data/levels.json', 'r') as fp:
        levels = json.load(fp)

    string += title + '\n'
    for level, talent in zip(levels, build):
        string += 'Level ' + str(level) + ' Talent ' + str(talent) + '\n'

    return string


def print_hero_builds(hero):
    string = ''

    string += ('-------------------------------- ' + hero
               + ' --------------------------------' + '\n')
    builds, titles = load_builds(hero)
    for build, title in zip(builds, titles):
        string += print_build(build, title)
        string += '\n'

    return string


def print_all_builds():
    heroes = get_heroes_list()

    for hero in heroes:
        print_hero_builds(hero)


def normalize_hero_name(hero):
    '''Clears string so that fits link'''
    hero = unicodedata.normalize('NFD', hero).encode('ascii', 'ignore')
    hero = str(hero.decode('utf-8'))
    hero = hero.replace(' ', '-')
    hero = hero.replace('.', '')
    hero = hero.replace('\'', '')
    return hero.lower()
