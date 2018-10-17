from .data import update_heroes_list, update_all_builds, print_all_builds

name = 'heroes build scrapper'


folder = 'data/builds'
if not os.path.exists(folder):
    os.makedirs(folder)

# Create levels.json file
if not os.path.exists('data/levels.json'):
    levels = [1, 4, 7, 10, 13, 16, 20]
    with open('data/levels.json', 'w') as fp:
        json.dump(levels, fp)

# Create heroes.json file
if not os.path.exists('data/heroes.json'):
    update_heroes_list()
