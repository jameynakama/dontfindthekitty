import sys
import webbrowser
from classes.panel import Panel


class Button(Panel):
    """
    A Panel that can also execute an action
    """
    def __init__(self, game, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.game = game

    def contains(self, x, y):
        return self.xpos <= x < self.xpos + self.width and self.ypos <= y < self.ypos + self.height


class ContinueButton(Button):
    def click(self):
        self.game.exit_game_loop = True


class ExitButton(Button):
    def click(self):
        sys.exit(0)


class TweetButton(Button):
    def __init__(self, game, intent_url="", *args, **kwargs):
        super(TweetButton, self).__init__(game, *args, **kwargs)
        self.intent_url = intent_url

    def click(self):
        webbrowser.open(self.intent_url)
