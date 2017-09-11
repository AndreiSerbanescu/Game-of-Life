import pygame as pg

import src.Settings as Settings

class Cell():

    def __init__(self, position):
        self.position = position
        self.bounds = pg.Rect(position.x * Settings.CELLSIZE, \
                         position.y * Settings.CELLSIZE, \
                          Settings.CELLSIZE, Settings.CELLSIZE)
        #self.is_alive = (position.x % 2 == 0)
        #self.is_alive = (position.x % 2 == 0 or position.y % 3 == 0)
        self.is_alive = False

    def draw(self, screen):

        if self.is_alive:
            pg.draw.rect(screen, (255, 0, 0), self.bounds)
