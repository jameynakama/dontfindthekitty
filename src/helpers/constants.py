import ConfigParser


class Constants:
    CONFIG = ConfigParser.ConfigParser()
    CONFIG.read('data/config.ini')

    FPS = 40
    ZOO_WIDTH = 50
    ZOO_HEIGHT = 30

    ADJECTIVES = [line.strip('\n') for line in open('data/adjectives.txt', 'r')]
    CREATURES = [line.strip('\n') for line in open('data/creatures.txt', 'r')]
