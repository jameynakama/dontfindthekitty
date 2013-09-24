import urllib
import webbrowser
import pygame
from classes.button import Button
from helpers.constants import Constants


class MessagePanel(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.length = Constants.MESSAGE_PANEL_HEIGHT

    def write_captures(self, window, captures):
        captures.reverse()
        self.buttons = []
        for i, creature in enumerate(captures):
            if not creature.creature == 'kitty':
                message_color = pygame.Color(255/(i+1), 255/(i+1), 255/(i+1))
            else:
                message_color = 'yellow'

            window.cursor = (0, self.ypos + i)
            window.write("You caught - ", fgcolor=message_color)
            window.write("[", fgcolor=message_color)
            creature_list_color = pygame.Color(
                creature.color.r/(i+1),
                creature.color.g/(i+1),
                creature.color.b/(i+1),
            )
            window.write(u"{character}".format(character=creature.character), fgcolor=creature_list_color)

            if not creature.creature == 'kitty':
                creature_description = "] - {adjective} {creature}".format(
                    adjective=creature.adjective,
                    creature=creature.creature,
                )
            else:
                creature_description = "] - the kitty! {sex} was {adjective}.".format(
                    sex=creature.sex.capitalize(),
                    adjective=creature.adjective,
                )

            window.write(creature_description, fgcolor=message_color)

            if creature_description[0] in Constants.VOWELS:
                twitter_text = u"I captured [{character}], an {adjective} {creature}.".format(
                    character=creature.character,
                    adjective=creature.adjective,
                    creature=creature.creature,
                )
            else:
                twitter_text = u"I captured [{character}], a {adjective} {creature}.".format(
                    character=creature.character,
                    adjective=creature.adjective,
                    creature=creature.creature,
                )
            twitter_url = 'https://twitter.com/intent/tweet?text={text}&hashtags={hashtags}&via={via}&url={url}'.format(
                text=urllib.quote(twitter_text.encode('utf8')),
                hashtags='dontfindthekitty',
                via='jameydeorio',
                url='http://jameydeorio.com',
            )
            tweet_button = Button(
                region=(Constants.ZOO_WIDTH - 4, self.ypos + i, 3, 1),
                fgcolor=pygame.Color(0, 150, 235),
                bgcolor=pygame.Color(225, 225, 225)
            )
            tweet_button.text = ' T'
            tweet_button.action = lambda: webbrowser.open(twitter_url)
            self.buttons.append(tweet_button)
            tweet_button.draw(window)
