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
            tweet_button = Button(region=(Constants.ZOO_WIDTH - 4, self.ypos + i, 2, 1), fgcolor='blue', bgcolor='white')
            # tweet_button.text = ' T'
            tweet_button.draw(window)

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
