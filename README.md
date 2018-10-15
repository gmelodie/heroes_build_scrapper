# heroes_build_scrapper

`heroes_build_scrapper` is a package designed to scrape character builds for
the [MOBA](https://en.wikipedia.org/wiki/Multiplayer_online_battle_arena)
game [Heroes of the Storm](https://heroesofthestorm.com/en-gb/). 

All builds are collected from [Icy Veins](https://www.icy-veins.com/).

## Installation

### Pip
You can install `heroes_build_scrapper` from the pip repositories

```
pip install heroes_build_scrapper
```


### Cloning the repo
In order to install `heroes_build_scrapper` manually you need to clone the repository
and then run the `setup.py` file:

```
$ git clone https://git@github.com:LTKills/heroes_build_scrapper.git
$ cd heroes_build_scrapper
$ python setup.py install
```

## Usage

Once you have installed the package you are ready to collect some builds. This is
done using the following code:

```
>>> import heroes_build_scrapper
>>> heroes_build_scrapper.update_heroes_list()
>>> heroes_build_scrapper.update_all_builds()
```

## Contributing

When contributing, add your nick and player tag to the [PLAYERS.md](PLAYERS.md) file. 

### Before Changing any Code

-   Please do not write any pull requests until an issue has been opened and assigned. 

-   Please do not write any pull requests for closed issues.

### Before Sending in a PR

-   Check that your PR and commits have useful titles that relate to the issue 

-   Check your spelling and grammar thoroughly

-   Have fun and happy open sourcing!

