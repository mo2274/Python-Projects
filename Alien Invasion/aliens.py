import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game, x, y):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.ship = ai_game.ship2
        self.image = pygame.image.load('images/alien2.bmp')
        self.rect = self.image.get_rect()
        '''
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        '''
        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update2(self):
        self.x += (self.setting.alien_speed * self.setting.fleet_direction)
        self.rect.x = self.x

    def update(self):
        if self.rect.x > self.ship.image_rect.x:
            self.x -= self.setting.alien_speed
            self.rect.x = self.x
        else:
            self.x += self.setting.alien_speed
            self.rect.x = self.x

        if self.rect.y > self.ship.image_rect.y:
            self.y -= self.setting.alien_speed
            self.rect.y = self.y
        else:
            self.y += self.setting.alien_speed
            self.rect.y = self.y

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def blitme(self):
        self.screen.blit(self.image, self.rect)
