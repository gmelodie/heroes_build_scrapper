
# Utilities' library
import unicodedata

'''
Gets a link, downloads page and gets soup
Returns beautifulsoup object
'''
def get_soup(link):
    page = requests.get(link)
    return BeautifulSoup(page.content, 'html.parser')


def print_build(levels, build, title):
    print('============== ' + str(title) + ' ==============')
    for level, talent in zip(levels, build):
        print('Level ' + str(level) + ' Talent ' + str(talent))

'''
Clears string so that fits link
'''
def normalize_hero_name(hero):
    hero = str(unicodedata.normalize('NFD', hero).encode('ascii', 'ignore'))
    hero = hero.replace(' ', '')
    hero = hero.replace("'", '')
    hero = hero[1:]
    return hero.lower()


