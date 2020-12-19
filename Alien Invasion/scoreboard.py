import pygame
from pygame.sprite import Group

from ship2 import Ship


class ScoreBoard():
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.rect
        self.setting = ai_game.setting
        self.stats = ai_game.stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 32)
        self.prep_score()
        self.prep_ships()

    def prep_score(self):
        score = str(self.stats.score)
        bg_color = (255, 255, 255, 255)
        self.score_image = self.font.render('Score (' + score + ')', True,
                                            self.text_color, bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.y = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.draw_ships()

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def draw_ships(self):
        self.ships.draw(self.screen)
