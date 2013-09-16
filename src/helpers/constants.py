import ConfigParser


class Constants:
    CONFIG = ConfigParser.ConfigParser()
    CONFIG.read('data/config.ini')

    ZOO_WIDTH = 40
    ZOO_HEIGHT = 25
