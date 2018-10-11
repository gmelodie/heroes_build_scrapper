#
# gets all builds for all heroes (prints or writes to file (json?)
from multiple import get_builds, print_build
import json

'''
Automatically scrape the list of heroes from icy-veins and
write it to a json file (heroes.json)
'''
def update_heroes_list():
    pass


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


heroes = ['uther', 'varian', 'ana', 'mephisto'] # scrape all heroes?
levels = [1, 4, 7, 10, 13, 16, 20] # levels in which one gets talents

for hero in heroes:
    print('-------------------------------- ' + hero + ' --------------------------------')
    builds, titles = get_builds(hero)
    for build, title in zip(builds, titles):
        print_build(levels, build, title)
