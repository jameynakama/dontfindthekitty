import random
import pygame

from constants import *


class Creature:
    def __init__(self):
        self.character = str(random.randint(33, 127))
        self.color = pygame.Color(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.sex = random.choice(('male', 'female'))
        self.xpos = random.randint(0, ZOO_WIDTH)
        self.ypos = random.randint(0, ZOO_HEIGHT)

    def move(self):
        newx = 0
        newy = 0

        while 1:
            direction = random.choice(((0, -1), (0, 1), (-1, 0), (1, 0)))
            newx = self.xpos + direction[0]
            newy = self.ypos + direction[1]
            if (0 <= newx < ZOO_WIDTH) and (0 <= newy < ZOO_HEIGHT):
                break

        self.xpos = newx
        self.ypos = newy

    def draw(self, window):
        window.putchar(
            self.character,
            x=self.xpos,
            y=self.ypos,
            fgcolor=self.color,
        )
