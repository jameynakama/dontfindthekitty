import sys
import pygame
import pygcurse

from constants import *
from creature import Creature


class Game:
    def __init__(self):
        self.window = pygcurse.PygcurseWindow(ZOO_WIDTH, ZOO_HEIGHT, "Don't Find The Kitty")
        self.window.autoupdate = False
        self.creatures = [Creature() for creature in range(3)]
        self.clock = pygame.time.Clock()

    def run(self):
        while 1:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            # input

            # compute
            for creature in self.creatures:
                creature.move()

            # draw
            self.window.fill(' ', 'black', 'black')
            self.render()

    def render(self):
        for creature in self.creatures:
            creature.draw(self.window)

        self.window.update()


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
