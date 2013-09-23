from helpers.constants import Constants


class Panel(object):
    """
    A panel that can be drawn to the screen. It can be made with or without a border or shadow.
    """
    def __init__(self, region, fgcolor, bgcolor, text=None, border=False, shadow=False):
        self.xpos = region[0]
        self.ypos = region[1]
        self.width = region[2]
        self.height = region[3]
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.border = border
        self.shadow = shadow
        self.text = text

    def draw(self, window):
        window.fill(
            '',
            fgcolor=self.fgcolor,
            bgcolor=self.bgcolor,
            region=(self.xpos, self.ypos, self.width, self.height)
        )

        if self.shadow:
            window.addshadow(region=(self.xpos, self.ypos, self.width, self.height))

        if self.border:
            for x in xrange(self.width):
                window.putchar('-', x=x + self.xpos, y=self.ypos, fgcolor='white', bgcolor='gray')
                window.putchar('-', x=x + self.xpos, y=self.ypos + self.height - 1, fgcolor='white', bgcolor='gray')
            for y in xrange(self.height):
                window.putchar('|', x=self.xpos, y=y + self.ypos, fgcolor='white', bgcolor='gray')
                window.putchar('|', x=self.xpos + self.width - 1, y=y + self.ypos, fgcolor='white', bgcolor='gray')
            window.putchar('+', x=self.xpos + self.width - 1, y=self.ypos, fgcolor='white')
            window.putchar('+', x=self.xpos + self.width - 1, y=self.ypos + self.height - 1, fgcolor='white')
            window.putchar('+', x=self.xpos, y=self.ypos + self.height - 1, fgcolor='white')
            window.putchar('+', x=self.xpos, y=self.ypos, fgcolor='white')

        if self.text:
            window.write(self.text, x=self.xpos, y=self.ypos, fgcolor=self.fgcolor, bgcolor=self.bgcolor)
