import ConfigParser
import os
import pygame


class Constants:
    DATA_DIR = os.path.abspath(os.path.join(__file__, '../../../data'))
    RES_DIR = os.path.abspath(os.path.join(__file__, '../../../res'))
    CONFIG = ConfigParser.ConfigParser()
    CONFIG.read(os.path.join(DATA_DIR, '../data/config.ini'))

    FPS = 40
    GAME_WIDTH = 60
    SCREEN_WIDTH = GAME_WIDTH
    SCREEN_HEIGHT = 28
    ZOO_WIDTH = GAME_WIDTH
    ZOO_HEIGHT = 20
    ZOO_BG_COLOR = pygame.Color(50, 50, 50)
    MESSAGE_PANEL_WIDTH = GAME_WIDTH
    MESSAGE_PANEL_HEIGHT = SCREEN_HEIGHT - ZOO_HEIGHT

    ADJECTIVES = [line.strip('\n') for line in open(os.path.join(DATA_DIR, 'adjectives.txt'), 'r')]
    CREATURES = [line.strip('\n') for line in open(os.path.join(DATA_DIR, '../data/creatures.txt'), 'r')]

    VOWELS = ['a', 'e', 'i', 'o', 'u']
