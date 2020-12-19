import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.bullet_speed = ai_game.setting.bullet_speed
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = (9, 60, 60)
        self.screen = ai_game.screen
        self.rect = pygame.Rect(0, 0, self.bullet_width,
                                self.bullet_height)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)


class Bullet_right(Bullet):
    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.rect.midright = ai_game.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.bullet_speed
        self.rect.x = self.x


class Bullet_up(Bullet):
    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.bullet_speed
        self.rect.y = self.y


class Bullet_down(Bullet):
    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.rect.midbottom = ai_game.ship.rect.midbottom
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.bullet_speed
        self.rect.y = self.y


class Bullet_left(Bullet):
    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.rect.midleft = ai_game.ship.rect.midleft
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.bullet_speed
        self.rect.x = self.x
