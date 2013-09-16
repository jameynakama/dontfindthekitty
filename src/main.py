import ConfigParser
import random
import sys
import pygame
import pygcurse

from helpers.constants import Constants
from helpers.zookeeper import Zookeeper
from classes.creatures import Creature
from classes.zoo_map import ZooMap


class Game:
    def __init__(self):
        self.window = pygcurse.PygcurseWindow(Constants.ZOO_WIDTH, Constants.ZOO_HEIGHT, "Don't Find The Kitty")
        self.window.autoupdate = False
        self.clock = pygame.time.Clock()

        pygame.mouse.set_visible(False)
        self.zookeeper = Zookeeper(Constants.CONFIG.get('zookeeper', 'character'))
        self.creatures = [Creature() for creature in range(100)]
        self.zoo_map = ZooMap()
        self.zoo_map.place_creatures(self.creatures)

    def run(self):
        while 1:
            self.clock.tick(Constants.CONFIG.getint('game', 'fps'))

            self.window.setscreencolors(None, 'black', clear=True)

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    sys.exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    xpos, ypos = self.window.getcoordinatesatpixel(event.pos)
                    print "{0}, {1}".format(xpos, ypos)
                    self.zoo_map = self.zookeeper.capture(self.zoo_map, xpos, ypos)

            # compute
            for row in self.zoo_map.grid:
                for thing in row:
                    if random.choice(range(Constants.CONFIG.getint('creatures', 'chance_to_move'))) == 1:
                        if isinstance(thing, Creature):
                            self.zoo_map = thing.move(self.zoo_map)

            # draw
            self.render()

    def render(self):
        self.zoo_map.draw(self.window)
        self.zookeeper.draw(self.window, pygame.mouse.get_pos())
        self.window.update()


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
