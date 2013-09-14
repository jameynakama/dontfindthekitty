import random
import sys

import pygame
from lib import pygcurse

from constants import *
from src.classes.Creature import Creature
from src.classes.ZooMap import ZooMap


class Game:
    def __init__(self):
        self.window = pygcurse.PygcurseWindow(ZOO_WIDTH, ZOO_HEIGHT, "Don't Find The Kitty")
        self.window.autoupdate = False
        self.clock = pygame.time.Clock()

        self.creatures = [Creature() for creature in range(100)]
        self.zoo_map = ZooMap()
        self.zoo_map.place_creatures(self.creatures)

    def run(self):
        while 1:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    sys.exit(0)

            # input

            # compute
            for creature in self.creatures:
                if random.choice(range(10)) == 1:
                    self.zoo_map = creature.move(self.zoo_map)

            # draw
            self.render()

    def render(self):
        self.window.fill(' ', 'black', 'black')

        self.zoo_map.draw(self.window)

        self.window.update()


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
