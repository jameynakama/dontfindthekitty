import random
import pygame

from helpers.constants import Constants


class Creature(object):
    def __init__(self):
        super(Creature, self).__init__()
        self.is_blocking = True

        character_range = range(33, 127)
        # Avoid creating '@' creatures
        character_range.remove(ord(Constants.CONFIG.get('zookeeper', 'character')))
        self.character = str(chr(random.choice(character_range)))
        self.adjective = random.choice(Constants.ADJECTIVES)
        self.creature = random.choice(Constants.CREATURES)
        self.color = pygame.Color(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.sex = random.choice(('male', 'female'))
        self.set_random_position()

    def set_random_position(self):
        self.xpos = random.randint(0, Constants.ZOO_WIDTH - 1)
        self.ypos = random.randint(0, Constants.ZOO_HEIGHT - 1)

    def move(self, zoo_map):
        direction = random.choice(((0, -1), (0, 1), (-1, 0), (1, 0)))
        newx = self.xpos + direction[0]
        newy = self.ypos + direction[1]
        if (0 <= newx < Constants.ZOO_WIDTH) and (0 <= newy < Constants.ZOO_HEIGHT):
            # If the move is within the map boundaries...
            if not zoo_map.is_occupied(newx, newy):
                # And another creature doesn't occupy this space...
                zoo_map.grid[self.ypos][self.xpos] = None
                self.xpos = newx
                self.ypos = newy
                zoo_map.grid[self.ypos][self.xpos] = self

    def draw(self, window):
        window.putchar(
            self.character,
            fgcolor=self.color,
            x=self.xpos,
            y=self.ypos,
        )

    def __repr__(self):
        return "[{character}] - {adjective} {creature}".format(
            character=self.character,
            adjective=self.adjective,
            creature=self.creature,
        )
