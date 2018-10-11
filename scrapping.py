
# Scrapes alextraza's build (has 2 builds)

from utils import print_build, normalize_hero_name
import requests
from bs4 import BeautifulSoup



'''
Scrape icy-veins for builds for the given hero
Returns two lists: one with other lists (each one for each build)
and the second one with the builds' titles
'''
def get_hero_builds(hero):
    builds = []

    hero = normalize_hero_name(hero)


    page_link = 'https://www.icy-veins.com/heroes/' + hero + '-build-guide'

    page = requests.get(page_link)
    soup = BeautifulSoup(page.content, 'html.parser')

    builds_tags = soup.find_all('div', class_='heroes_tldr_talents')
    build_title_tags = soup.find_all('h4', class_='toc_no_parsing')

    # strip ' (talent calculator link)' from title
    strip_size = (len(' (talent calculator link)') + 1)
    build_titles = [title.get_text()[:-strip_size] for title in build_title_tags]

    # sometimes there is a '\n' we need to strip, if last letter is a 'd'
    # then we striped the '\n', else we striped a 'd' we need to put back
    build_titles = [title + 'd' if len(title) >= 1 and title[-1] is not 'd' else title for title in build_titles]

    for build_number, build_tag in enumerate(builds_tags):
        build = []
        talent_tiers = build_tag.find_all('span', class_= 'heroes_tldr_talent_tier_visual')

        for tier in talent_tiers:
            children = tier.find_all('span')
            for j, child in enumerate(children):
                if('heroes_tldr_talent_tier_yes' in child['class']):
                    build.append(j+1)
        builds.append(build[:])

    # remove empty titles
    build_titles = [title for title in build_titles if title != '']

    return builds, build_titles
