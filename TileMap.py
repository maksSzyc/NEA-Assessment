import pygame
from os import path
from Settings import *
from Game import *

class Map:
    def __init__(self):
        # call Map class and load tiles text folder
        self.game_folder = path.dirname(__file__)
        self.filename = path.join(self.game_folder, "tiles")
        # append tiles to a list
        self.data = []
        with open(self.filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        # set width settings to allow for camera manipulation
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * T_SIZE
        self.height = self.tileheight * T_SIZE

class WorldShift:
    def __init__(self, width, height):
        # create camera rectangle
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    # manipulate existing rectangles
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        # set camera movement as opposite
        x = -target.rect.x + int(SCREEN_WIDTH / 2)
        y = -target.rect.y + int(SCREEN_HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - SCREEN_WIDTH), x)
        y = max(-(self.height - SCREEN_HEIGHT), y)
        self.camera = pygame.Rect(x, y, self.width, self.height)
