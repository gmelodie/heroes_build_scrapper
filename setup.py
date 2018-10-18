from setuptools import setup, find_packages


with open('requirements.txt') as fp:
    required = fp.read().splitlines()

setup(
    install_requires=required,
    name='heroes_build_scrapper',
    version='1.1.3',
    author='Gabriel Cruz',
    author_email=('gabs.oficial98@gmail.com'),
    packages=find_packages('src'),
    package_dir={"": "src"},
    description='A library for scraping builds for Heroes of the Storm heroes.',
)
