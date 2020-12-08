import pygame

class Bomb():
    def __init__(self, x):
        self.x = x
        self.y = 0
        self.raduis = 15
        self.color = (0, 0, 255)
        self.thickness = 5
