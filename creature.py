import random
import pygame

from constants import *
from Thing import Thing


class Creature(Thing):
    def __init__(self):
        self.character = str(chr(random.randint(33, 127)))
        self.color = pygame.Color(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.sex = random.choice(('male', 'female'))
        self.xpos = random.randint(0, ZOO_WIDTH - 1)
        self.ypos = random.randint(0, ZOO_HEIGHT - 1)

    def move(self, zoo_map):
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

        zoo_map.grid[self.ypos][self.xpos] = self
        return zoo_map

    def draw(self, window):
        window.putchar(
            self.character,
            x=self.xpos,
            y=self.ypos,
            fgcolor=self.color,
        )
