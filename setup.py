import os
from setuptools import setup, find_packages

folder = 'data/builds'
if not os.path.exists(folder):
    os.makedirs(folder)

with open('requirements.txt') as fp:
    required = fp.read().splitlines()

setup(
    install_requires=required,
    name='heroes_build_scrapper',
    version='0.0.1',
    author='Gabriel Cruz',
    author_email=('email'),
    packages=find_packages('src'),
    package_dir={"": "src"},
    description='A library for scraping builds for Heroes of the Storm heroes.')