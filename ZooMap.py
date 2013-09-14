from constants import *
from Thing import Thing


class ZooMap:
    def __init__(self):
        self.grid = [[Thing() for x in range(ZOO_WIDTH)] for y in range(ZOO_HEIGHT)]

    def draw(self, window):
        for row in self.grid:
            for thing in row:
                thing.draw(window)
