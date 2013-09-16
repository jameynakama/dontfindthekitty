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
        self.cursor = Zookeeper(Constants.CONFIG.get('zookeeper', 'character'))
        self.creatures = [Creature() for creature in range(100)]
        self.zoo_map = ZooMap()
        self.zoo_map.place_creatures(self.creatures)

    def run(self):
        while 1:
            self.clock.tick(int(Constants.CONFIG.get('game', 'fps')))

            self.window.setscreencolors(None, 'black', clear=True)

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    sys.exit(0)

            # compute
            for creature in self.creatures:
                if random.choice(range(10)) == 1:
                    self.zoo_map = creature.move(self.zoo_map)

            # draw
            self.render()

    def render(self):
        self.zoo_map.draw(self.window)

        self.cursor.draw(self.window, pygame.mouse.get_pos())

        self.window.update()


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
