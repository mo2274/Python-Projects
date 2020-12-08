import pygame
import sys
from random import randint

from ship import Ship
from setting import Settings
from bullet import Bullet
from bombs import Bomb


class AlienInvasion():
    """sumary_line"""
    def __init__(self):
        pygame.init()
        self.setting = Settings()
        self.background_color = self.setting.color
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height
        pygame.display.set_caption("Aliens Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bombs = []
        self.counter = 0
        self.bomb_speed = 2

    def _add_bulets(self):
        if len(self.bullets) < self.setting.num_of_bullets:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _show_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.bullets.update()
        # remove old bullets
        for bullet in self.bullets.copy():
            if bullet.bullet_rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_keyDown_events(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_SPACE:
            self._add_bulets()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyUp_events(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = False
          
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keyDown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyUp_events(event)

    def _draw_bombs(self):
        if self.counter % 40 == 0:
            x = randint(0, 1300)
            bomb = Bomb(x)
            self.bombs.append(bomb)
        self.counter += 1

    def _show_bombs(self):
        for bomb in self.bombs:
            pygame.draw.circle(self.screen, bomb.color, (bomb.x, bomb.y), bomb.raduis, bomb.thickness)
            bomb.y += self.bomb_speed

    def _update_screen(self):
        self.screen.fill(self.background_color)
        self.ship.update()
        self.ship.blitme()
        self._show_bullets()
        self._draw_bombs()
        self._show_bombs()
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

                    