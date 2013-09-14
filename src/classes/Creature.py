import random
import pygame

from src.constants import *
from src.classes.Thing import Thing


class Creature(Thing):
    def __init__(self):
        super(Creature, self).__init__()
        self.is_blocking = True

        self.character = str(chr(random.randint(33, 127)))
        self.color = pygame.Color(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.sex = random.choice(('male', 'female'))
        self.set_random_position()

    def set_random_position(self):
        self.xpos = random.randint(0, ZOO_WIDTH - 1)
        self.ypos = random.randint(0, ZOO_HEIGHT - 1)

    def move(self, zoo_map):
        direction = random.choice(((0, -1), (0, 1), (-1, 0), (1, 0)))
        newx = self.xpos + direction[0]
        newy = self.ypos + direction[1]
        if (0 <= newx < ZOO_WIDTH) and (0 <= newy < ZOO_HEIGHT):
            # If the move is within the map boundaries...
            if not zoo_map.is_occupied(newx, newy):
                # And another creature doesn't occupy this space...
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
