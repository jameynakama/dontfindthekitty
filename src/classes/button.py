from classes.panel import Panel


class Button(Panel):
    def __init__(self, action=lambda: None, *args, **kwargs):
        super(Button, self).__init__(action, *args, **kwargs)
        self.action = action

    def contains(self, x, y):
        return self.xpos <= x < self.xpos + self.width and self.ypos <= y < self.ypos + self.height

    def execute(self):
        self.action()
