import pygame


class Ship():
    """
    docstring
    """
    def __init__(self, ai_game):
        self.speed = 3
        self.ships = ['images/Ship1.bmp', 'images/Ship2.bmp',
                      'images/Ship3.bmp', 'images/Ship4.bmp']
        self.image = pygame.image.load(self.ships[1])
        self.rect = self.image.get_rect()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False
        self.direction = 0

    def blitme(self):
        self.image = pygame.image.load(self.ships[self.direction])
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_up:
            self.direction = 0
            if self.rect.top > self.screen_rect.top:
                self.rect.y -= self.speed
        if self.move_down:
            self.direction = 2
            if self.rect.bottom < self.screen_rect.bottom:
                self.rect.y += self.speed
        if self.move_right:
            self.direction = 1
            if self.rect.right < self.screen_rect.right:
                self.rect.x += self.speed
        if self.move_left:
            self.direction = 3
            if self.rect.left > self.screen_rect.left:
                self.rect.x -= self.speed

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
