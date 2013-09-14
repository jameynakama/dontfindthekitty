import random
import pygame

from constants import *


class Creature:
    def __init__(self, window):
        self.character = unichr(random.randint(33, 127))
        self.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.sex = random.choice(('male', 'female'))
        self.xpos = random.randint(0, ZOO_WIDTH)
        self.ypos = random.randint(0, ZOO_HEIGHT)

    def draw(self, window):
        window.write(
            self.character,
            x=self.xpos,
            y=self.ypos,
            fgcolor=self.color,
        )

    def move(self):
        newx = self.xpos - 1
        newy = self.ypos - 1
        if (0 < newx < ZOO_WIDTH) and (0 < newy < ZOO_HEIGHT):
            self.xpos -= 0
            self.ypos += 1
