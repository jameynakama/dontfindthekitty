from helpers.constants import Constants


class ZooMap(object):
    def __init__(self):
        self.grid = [[None for x in range(Constants.ZOO_WIDTH)] for y in range(Constants.ZOO_HEIGHT)]

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
            for creature in row:
                if creature:
                    creature.draw(window)

    def is_occupied(self, xpos, ypos):
        return self.grid[ypos][xpos]

    def remove_creature(self, creature):
        self.grid[creature.ypos][creature.xpos] = None
