import pygame


class Ship2():
    """
    docstring
    """
    def __init__(self, ai_game):
        self.speed = 3
        self.image = pygame.image.load('images/Ship33.bmp')
        self.image_rect = self.image.get_rect()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image_rect.bottom = self.screen_rect.bottom
        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)

    def update(self):
        if self.move_up:
            if self.image_rect.top > self.screen_rect.top:
                self.image_rect.y -= self.speed
        if self.move_down:
            if self.image_rect.bottom < self.screen_rect.bottom:
                self.image_rect.y += self.speed
        if self.move_right:
            if self.image_rect.right < self.screen_rect.right:
                self.image_rect.x += self.speed
        if self.move_left:
            if self.image_rect.left > self.screen_rect.left:
                self.image_rect.x -= self.speed       
