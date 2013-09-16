from helpers.constants import *
from classes.creatures import Thing


class ZooMap:
    def __init__(self):
        self.grid = [[Thing() for x in range(ZOO_WIDTH)] for y in range(ZOO_HEIGHT)]

    def place_creatures(self, creatures):
        for creature in creatures:
            while 1:
                if not self.is_occupied(creature.xpos, creature.ypos):
                    self.grid[creature.ypos][creature.xpos] = creature
                    break
                else:
                    creature.set_random_position()

    def draw(self, window):
        for row in self.grid:
            for thing in row:
                thing.draw(window)

    def is_occupied(self, xpos, ypos):
        return self.grid[ypos][xpos].is_blocking
