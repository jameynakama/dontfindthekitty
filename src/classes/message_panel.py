import pygame
from helpers.constants import Constants


class MessagePanel(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.length = Constants.MESSAGE_PANEL_HEIGHT

    def write_captures(self, window, captures):
        for i, creature in enumerate(captures):
            window.cursor = (0, self.ypos+i)
            message_color = pygame.Color(255/(i+1), 255/(i+1), 255/(i+1))
            window.write("You caught - ", fgcolor=message_color)
            window.write("[", fgcolor=message_color)
            creature_list_color = pygame.Color(
                creature.color.r/(i+1),
                creature.color.g/(i+1),
                creature.color.b/(i+1),
            )
            window.write(u"{character}".format(character=creature.character), fgcolor=creature_list_color)
            creature_description = "] - {adjective} {creature}".format(
                adjective=creature.adjective,
                creature=creature.creature,
            )
            window.write(creature_description, fgcolor=message_color)
