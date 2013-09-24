import random
import urllib
import pygame

from helpers.constants import Constants


class Creature(object):
    character_range = range(33, 127) + range(161, 440)
    characters = [unichr(i) for i in character_range]
    # Avoid creating '@' creatures
    characters.remove(unichr(ord(Constants.CONFIG.get('zookeeper', 'character'))))

    def __init__(self, creature=None):
        super(Creature, self).__init__()
        self.is_blocking = True

        random.shuffle(Constants.CREATURES)
        self.creature = creature if creature else Constants.CREATURES.pop()

        random.shuffle(Creature.characters)
        self.character = Creature.characters.pop()

        random.shuffle(Constants.ADJECTIVES)
        self.adjective = Constants.ADJECTIVES.pop()

        self.color = pygame.Color(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.sex = random.choice(('he', 'she'))
        self.set_random_position()

    def set_random_position(self):
        self.xpos = random.randint(1, Constants.ZOO_WIDTH - 2)
        self.ypos = random.randint(1, Constants.ZOO_HEIGHT - 2)

    def move(self, zoo_map):
        direction = random.choice(((0, -1), (0, 1), (-1, 0), (1, 0)))
        newx = self.xpos + direction[0]
        newy = self.ypos + direction[1]
        if (1 <= newx < Constants.ZOO_WIDTH - 1) and (1 <= newy < Constants.ZOO_HEIGHT - 1):
            # If the move is within the zoo boundaries...
            if not zoo_map.is_occupied(newx, newy):
                # And another creature doesn't occupy this space...
                zoo_map.grid[self.ypos][self.xpos] = None
                self.xpos = newx
                self.ypos = newy
                zoo_map.grid[self.ypos][self.xpos] = self

    def draw(self, window):
        window.write(
            self.character,
            fgcolor=self.color,
            bgcolor=Constants.ZOO_BG_COLOR,
            x=self.xpos,
            y=self.ypos,
        )

    def get_twitter_intent_url(self):
        if self.adjective[0] in Constants.VOWELS:
            twitter_text = u"I captured [{character}], an {adjective} {creature}.".format(
                character=self.character,
                adjective=self.adjective,
                creature=self.creature,
            )
        else:
            twitter_text = u"I captured [{character}], a {adjective} {creature}.".format(
                character=self.character,
                adjective=self.adjective,
                creature=self.creature,
            )
        return 'https://twitter.com/intent/tweet?text={text}&hashtags={hashtags}&url={url}'.format(
            text=urllib.quote(twitter_text.encode('utf8')),
            hashtags='dontfindthekitty',
            url='http://jameydeorio.com',
        )
