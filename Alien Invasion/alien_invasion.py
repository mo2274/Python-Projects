import pygame
import sys

from ship import Ship
from setting import Settings
from bullet import Bullet
from aliens import Alien


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
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _add_bulets(self):
        if len(self.bullets) < self.setting.num_of_bullets:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _show_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.bullets.update()
        self.remove_old_bullets()

    def remove_old_bullets(self):
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

    def _create_fleet(self):
        """ create a fleet of aliens """
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)

    def _create_alien(self, alien_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _update_screen(self):
        self.screen.fill(self.background_color)
        self.ship.update()
        self.ship.blitme()
        self._show_bullets()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
