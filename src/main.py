#!/usr/bin/env python

import os
import sys
sys.path.append(os.path.abspath('lib'))

import random
import urllib
import webbrowser
import pygame
import pygcurse
from classes.buttons import Button, ContinueButton, ExitButton, TweetButton
from classes.message_panel import MessagePanel
from classes.panel import Panel

from helpers.constants import Constants
from classes.zookeeper import Zookeeper
from classes.creature import Creature
from classes.zoo_map import ZooMap


# TODO: Tweet individual captures is broken
# TODO: Display kitty when player wins, too
# TODO: End screen is too big and clunky. Refactor.
# TODO: Game modes: 10, 25, 50, 100 creatures and Game B (hints)


class Game(object):
    def __init__(self):
        self.window = pygcurse.PygcurseWindow(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, "Don't Find The Kitty")
        pygame.mouse.set_visible(False)
        self.window.autoupdate = False
        self.clock = pygame.time.Clock()

        font_name = Constants.CONFIG.get('game', 'font')
        font_size = Constants.CONFIG.getint('game', 'font_size')
        self.window.font = pygame.font.Font(os.path.join(Constants.RES_DIR, font_name), font_size)

        self.zookeeper = Zookeeper(Constants.CONFIG.get('zookeeper', 'character'))
        self.creatures = [Creature() for n in range(10)]
        self.kitty = Creature(creature='kitty')
        self.creatures.append(self.kitty)
        self.zoo_map = ZooMap()
        self.zoo_map.place_creatures(self.creatures)
        self.message_panel = MessagePanel(0, Constants.ZOO_HEIGHT)
        self.last_captured = Creature()

        self.exit_game_loop = False

    def run(self):
        while not self.exit_game_loop:
            self.clock.tick(Constants.FPS)

            self.window.setscreencolors(None, 'black', clear=True)
            self.window.fill(bgcolor=Constants.ZOO_BG_COLOR, region=(1, 1, Constants.ZOO_WIDTH - 2, Constants.ZOO_HEIGHT - 2))

            # input
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    sys.exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    xpos, ypos = self.window.getcoordinatesatpixel(event.pos)
                    if 0 < xpos < Constants.ZOO_WIDTH and 0 < ypos < Constants.ZOO_HEIGHT:
                        captured = self.zookeeper.capture(self.zoo_map, xpos, ypos)
                        if captured:
                            self.last_captured = captured
                            self.creatures.remove(captured)
                        if self.last_captured.creature == 'kitty':
                            self.end_screen(won=False)
                            break
                        if len(self.creatures) == 1:
                            self.end_screen(won=True)
                            break
                    for button in self.message_panel.buttons:
                        if button.contains(xpos, ypos):
                            button.click()

            # compute
            for row in self.zoo_map.grid:
                for thing in row:
                    if thing and random.choice(range(Constants.CONFIG.getint('creatures', 'chance_to_move'))) == 1:
                        thing.move(self.zoo_map)

            # draw
            self.render()

    def render(self):
        self.zoo_map.draw(self.window)
        self.message_panel.write_captures(self, self.zookeeper.captures[-self.message_panel.length:])
        self.zookeeper.draw(self.window, pygame.mouse.get_pos())
        self.window.update()

    def end_screen(self, won=False):
        kitty_panel = Panel(region=(12, 5, 36, 5), fgcolor='white', bgcolor='gray', border=True, shadow=True)
        kitty_panel.text = "You won!" if won else "You lost!"
        kitty_panel.text += ' Play again?'

        buttons = []

        yes_button = ContinueButton(self, region=(18, 8, 6, 1), fgcolor=pygame.Color(0, 100, 0), bgcolor='white')
        yes_button.text = ' yes'
        buttons.append(yes_button)

        no_button = ExitButton(self, region=(28, 8, 6, 1), fgcolor=pygame.Color(100, 0, 0), bgcolor='white')
        no_button.text = '  no'
        buttons.append(no_button)

        tweet_button = TweetButton(self, region=(38, 8, 6, 1), fgcolor=pygame.Color(0, 0, 255), bgcolor='white')
        tweet_button.text = 'tweet'
        if won:
            twitter_text = u"I didn't find the kitty [{0}]!".format(self.kitty.character)
        else:
            twitter_text = u"I found the kitty [{0}]!".format(self.kitty.character)
        twitter_text += " {sex} was {adjective}.".format(
            sex=self.kitty.sex.capitalize(),
            adjective=self.kitty.adjective,
        )
        twitter_intent_url = 'https://twitter.com/intent/tweet?text={text}&hashtags={hashtags}&url={url}'.format(
            text=urllib.quote(twitter_text.encode('utf8')),
            hashtags='dontfindthekitty',
            url='http://jameydeorio.com',
        )
        tweet_button.intent_url = twitter_intent_url
        buttons.append(tweet_button)

        while not self.exit_game_loop:
            self.clock.tick(Constants.FPS)

            self.window.setscreencolors(None, 'black', clear=True)
            self.window.fill(bgcolor=Constants.ZOO_BG_COLOR, region=(1, 1, Constants.ZOO_WIDTH - 2, Constants.ZOO_HEIGHT - 2))

            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    sys.exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    xpos, ypos = self.window.getcoordinatesatpixel(event.pos)
                    if 0 < xpos < Constants.ZOO_WIDTH and 0 < ypos < Constants.ZOO_HEIGHT:
                        for button in buttons:
                            if button.contains(xpos, ypos):
                                button.click()

            self.zoo_map.draw(self.window)
            self.message_panel.write_captures(self, self.zookeeper.captures[-self.message_panel.length:])

            kitty_panel.draw(self.window)

            for button in buttons:
                button.draw(self.window)

            self.zookeeper.draw(self.window, pygame.mouse.get_pos())
            self.window.update()

    def restart(self):
        self.exit_game_loop = True


def main():
    while 1:
        game = Game()
        game.run()


if __name__ == '__main__':
    main()
