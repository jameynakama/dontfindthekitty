import pygame

from constants import *

class Zookeeper:
    def __init__(self, character):
        self.character = character
        self.color = pygame.Color(255, 255, 255)
        self.capturing = False

    def draw(self, window, position):
        color = self.color
        if self.capturing:
            color = 'yellow'
        xpos, ypos = window.getcoordinatesatpixel(position)
        window.putchar(self.character, fgcolor=color, bgcolor=None, x=xpos, y=ypos)
