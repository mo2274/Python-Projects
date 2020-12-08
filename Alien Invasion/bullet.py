import pygame
import sys
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.bullet_speed = 5
        self.bullet_width = 6
        self.bullet_height = 20
        self.bullet_color = (9, 60, 60)
        self.screen = ai_game.screen
        self.bullet_rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.bullet_rect.midtop = ai_game.ship.image_rect.midtop
        self.y = float(self.bullet_rect.y)

    def update(self):
        self.y -= self.bullet_speed
        self.bullet_rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.bullet_rect)

