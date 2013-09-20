import ConfigParser
import os
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
        self.window = pygcurse.PygcurseWindow(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, "Don't Find The Kitty")
        self.window.font = pygame.font.Font(os.path.join(Constants.RES_DIR, Constants.CONFIG.get('game', 'font')), 12)
        self.window.autoupdate = False
        self.clock = pygame.time.Clock()

        pygame.mouse.set_visible(False)
        self.zookeeper = Zookeeper(Constants.CONFIG.get('zookeeper', 'character'))
        self.creatures = [Creature() for creature in range(30)]
        self.zoo_map = ZooMap()
        self.zoo_map.place_creatures(self.creatures)

    def run(self):
        while 1:
            self.clock.tick(Constants.FPS)

            self.window.setscreencolors(None, 'black', clear=True)

            # input
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    sys.exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    xpos, ypos = self.window.getcoordinatesatpixel(event.pos)
                    self.last_captured = self.zookeeper.capture(self.zoo_map, xpos, ypos)

            # compute
            for row in self.zoo_map.grid:
                for thing in row:
                    if thing and random.choice(range(Constants.CONFIG.getint('creatures', 'chance_to_move'))) == 1:
                        thing.move(self.zoo_map)

            # draw
            self.render()

    def render(self):
        for x in xrange(Constants.ZOO_WIDTH):
            self.window.putchar('#', x=x, y=0)
            self.window.putchar('#', x=x, y=Constants.ZOO_HEIGHT - 1)
        for y in xrange(Constants.ZOO_HEIGHT):
            self.window.putchar('#', x=0, y=y)
            self.window.putchar('#', x=Constants.ZOO_WIDTH - 1, y=y)
        self.zoo_map.draw(self.window)
        self.zookeeper.draw(self.window, pygame.mouse.get_pos())
        if getattr(self, 'last_captured', None):
            self.window.write(self.last_captured.__repr__(), fgcolor='white', x=0, y=Constants.ZOO_HEIGHT)
        self.window.update()


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
