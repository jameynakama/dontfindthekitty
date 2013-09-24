import pygame
from classes.buttons import TweetButton
from helpers.constants import Constants


# TODO: Refactor messaging based on winning
# TODO: figure out how to display long lines


class MessagePanel(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.length = Constants.MESSAGE_PANEL_HEIGHT
        self.buttons = []
        self.captures = []

    def add_capture(self, game, creature):
        self.captures.insert(0, creature)

        tweet_button = TweetButton(
            game=game,
            intent_url=creature.get_twitter_intent_url(),
            region=(Constants.ZOO_WIDTH - 4, 0, 3, 1),  # ypos is calculated in write_captures
            fgcolor=pygame.Color(0, 150, 235),
            bgcolor=pygame.Color(225, 225, 225)
        )
        tweet_button.text = ' T'
        tweet_button.intent_url = creature.get_twitter_intent_url()
        self.buttons.insert(0, tweet_button)

        if len(self.captures) > Constants.MESSAGE_PANEL_HEIGHT:
            self.captures.pop()
            self.buttons.pop()

    def write_captures(self, game):
        """
        Draws the captures and associated tweet buttons to the screen
        """
        for i, creature in enumerate(self.captures):
            game.window.cursor = (0, self.ypos + i)
            if not creature.creature == 'kitty':
                message_color = pygame.Color(255/(i+1), 255/(i+1), 255/(i+1))
                game.window.write("You caught - ", fgcolor=message_color)
            else:
                if game.won:
                    message_color = 'green'
                    game.window.write("You didn't catch - ", fgcolor=message_color)
                else:
                    message_color = 'red'
                    game.window.write("You caught - ", fgcolor=message_color)

            game.window.write("[", fgcolor=message_color)
            creature_list_color = pygame.Color(
                creature.color.r/(i+1),
                creature.color.g/(i+1),
                creature.color.b/(i+1),
            )
            game.window.write(u"{character}".format(character=creature.character), fgcolor=creature_list_color)

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

            game.window.write(creature_description, fgcolor=message_color)

            self.buttons[i].ypos = self.ypos + i
            self.buttons[i].draw(game.window)
