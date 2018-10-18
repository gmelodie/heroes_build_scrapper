
from .utils import print_build, normalize_hero_name, get_soup
import requests
from bs4 import BeautifulSoup


def get_builds_titles(build_title_tags):
    build_titles = []

    build_titles_aux = [title.get_text() for title in build_title_tags]

    # remove empty titles
    build_titles = [title for title in build_titles_aux if title != '']

    return build_titles

def get_hero_builds(hero):
    '''Scrape icy-veins for builds for the given hero.

    Returns two lists: one with other lists (each one for each build) and the
    second one with the builds' titles
    '''
    builds = []
    hero = normalize_hero_name(hero)
    link = 'https://www.icy-veins.com/heroes/' + hero + '-build-guide'
    soup = get_soup(link)

    builds_tags = soup.find_all('div', class_='heroes_build_talents')
    build_title_tags = soup.find_all('h3', class_='toc_no_parsing')

    build_titles = get_builds_titles(build_title_tags)

    for build_number, build_tag in enumerate(builds_tags):
        build = []
        talent_tiers = build_tag.find_all('span', class_= 'heroes_build_talent_tier_visual')

        # find out which block is painted with green (chosen talent)
        for tier in talent_tiers:
            children = tier.find_all('span')
            for j, child in enumerate(children):
                if('heroes_build_talent_tier_yes' in child['class']):
                    build.append(j+1)

        # append whole build to builds list
        builds.append(build[:])

    return builds, build_titles
