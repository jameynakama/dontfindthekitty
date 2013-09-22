class Panel(object):
    """
    Creates a panel that can be drawn to the screen. It can be made with or without a border or shadow.
    """
    def __init__(self, xpos, ypos, width, height, fgcolor, bgcolor, border=False, shadow=False):
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.border = border
        self.shadow = shadow

    def draw(self, window):
        window.fill(
            ' ',
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
