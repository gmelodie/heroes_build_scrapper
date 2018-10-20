
# Utilities' library
import unicodedata
import requests
import json
from bs4 import BeautifulSoup

def get_soup(link):
    '''Gets a link, downloads page and gets soup
    Returns beautifulsoup object
    '''
    page = requests.get(link)
    return BeautifulSoup(page.content, 'html.parser')


def load_builds(hero):
    '''Loads builds for a hero'''
    hero = normalize_hero_name(hero)
    filename = 'data/builds/' + hero + '.json'
    load_list = []
    builds = []
    builds_titles = []

    with open(filename, 'r') as fp:
        load_list = json.load(fp)

    for i in range(0, len(load_list) - 1, 2):
        builds.append(load_list[i])
        builds_titles.append(load_list[i + 1])

    return builds, builds_titles


def get_heroes_list():
    with open('data/heroes.json', 'r') as fp:
        heroes = json.load(fp)

    return heroes


def print_build(levels, build, title):
    print(title)
    for level, talent in zip(levels, build):
        print('Level ' + str(level) + ' Talent ' + str(talent))


def print_hero_builds(hero):
    with open('data/levels.json', 'r') as fp:
        levels = json.load(fp)

    print('-------------------------------- ' + hero + ' --------------------------------')
    builds, titles = load_builds(hero)
    for build, title in zip(builds, titles):
        print_build(levels, build, title)


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

