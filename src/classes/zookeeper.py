import pygame


class Zookeeper(object):
    def __init__(self, character):
        self.character = character
        self.color = pygame.Color(255, 255, 0)
        self.captures = []

    def draw(self, window, position):
        self.xpos, self.ypos = window.getcoordinatesatpixel(position)
        window.putchar(self.character, fgcolor=self.color, bgcolor=None, x=self.xpos, y=self.ypos)

    def capture(self, zoo_map, xpos, ypos):
        thing = zoo_map.grid[ypos][xpos]
        if thing:
            zoo_map.remove_creature(thing)
            self.captures.append(thing)
            return thing
        return None
