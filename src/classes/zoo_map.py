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
        for x in xrange(Constants.ZOO_WIDTH):
            window.putchar('#', x=x, y=0, fgcolor='white')
            window.putchar('#', x=x, y=Constants.ZOO_HEIGHT - 1, fgcolor='white')
        for y in xrange(Constants.ZOO_HEIGHT):
            window.putchar('#', x=0, y=y, fgcolor='white')
            window.putchar('#', x=Constants.ZOO_WIDTH - 1, y=y, fgcolor='white')
        for row in self.grid:
            for creature in row:
                if creature:
                    creature.draw(window)

    def is_occupied(self, xpos, ypos):
        return self.grid[ypos][xpos]

    def remove_creature(self, creature):
        self.grid[creature.ypos][creature.xpos] = None
