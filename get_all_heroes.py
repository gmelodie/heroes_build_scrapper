





# gets all builds for all heroes (prints or writes to file (json?)
from multiple import get_builds, print_build

heroes = ['uther', 'varian', 'ana', 'mephisto'] # scrape all heroes?
levels = [1, 4, 7, 10, 13, 16, 20] # levels in which one gets talents

for hero in heroes:
    print('-------------------------------- ' + hero + ' --------------------------------')
    builds, titles = get_builds(hero)
    for build, title in zip(builds, titles):
        print_build(levels, build, title)
