
# Utilities' library
import unicodedata
import requests
from bs4 import BeautifulSoup

def get_soup(link):
    '''Gets a link, downloads page and gets soup
    Returns beautifulsoup object
    '''
    page = requests.get(link)
    return BeautifulSoup(page.content, 'html.parser')


def print_build(levels, build, title):
    print('============== ' + str(title) + ' ==============')
    for level, talent in zip(levels, build):
        print('Level ' + str(level) + ' Talent ' + str(talent))

def normalize_hero_name(hero):
    '''Clears string so that fits link'''
    hero = unicodedata.normalize('NFD', hero).encode('ascii', 'ignore')
    hero = str(hero.decode('utf-8'))
    hero = hero.replace(' ', '-')
    hero = hero.replace('.', '')
    hero = hero.replace('\'', '')
    return hero.lower()

