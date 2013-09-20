import ConfigParser
import os


class Constants:
    DATA_DIR = os.path.abspath(os.path.join(__file__, '../../../data'))
    RES_DIR = os.path.abspath(os.path.join(__file__, '../../../res'))
    CONFIG = ConfigParser.ConfigParser()
    CONFIG.read(os.path.join(DATA_DIR, '../data/config.ini'))

    FPS = 40
    SCREEN_WIDTH = 50
    SCREEN_HEIGHT = 30
    ZOO_WIDTH = 50
    ZOO_HEIGHT = 20

    ADJECTIVES = [line.strip('\n') for line in open(os.path.join(DATA_DIR, 'adjectives.txt'), 'r')]
    CREATURES = [line.strip('\n') for line in open(os.path.join(DATA_DIR, '../data/creatures.txt'), 'r')]
