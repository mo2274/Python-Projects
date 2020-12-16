""" The ship.py fle contains the Ship class. The Ship class has an __init__()
method, an update() method to manage the ship’s position, and a blitme()
method to draw the ship to the screen. The image of the ship is stored in
ship.bmp, which is in the images folder.
"""
import pygame


class Ship():
    """
    docstring
    """
    def __init__(self, ai_game):
        """sumary_line"""
        self.screen_width = ai_game.width
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/Ship3.bmp')
        self.image_rect = self.image.get_rect()
        self.image_rect.midbottom = self.screen_rect.midbottom
        self.move_right = False
        self.move_left = False
        self.speed = 2

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.image_rect)

    def update(self):
        if self.move_right:
            if self.image_rect.right < self.screen_rect.right:
                self.image_rect.x += self.speed
        if self.move_left:
            if self.image_rect.left > self.screen_rect.left:
                self.image_rect.x -= self.speed
