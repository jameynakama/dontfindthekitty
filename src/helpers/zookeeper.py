import pygame

from constants import *

class Zookeeper:
    def __init__(self, character):
        self.character = character
        self.color = pygame.Color(255, 255, 255)

    def draw(self, window, position):
        xpos, ypos = window.getcoordinatesatpixel(position)
        window.putchar(self.character, fgcolor=self.color, bgcolor=None, x=xpos, y=ypos)
