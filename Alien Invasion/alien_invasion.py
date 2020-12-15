import pygame
import sys
from random import randint

from ship import Ship
from setting import Settings
from bullet import Bullet_hroz
from aliens import Alien
from ship2 import Ship2


class AlienInvasion():
    """sumary_line"""
    def __init__(self):
        pygame.init()
        self.setting = Settings()
        self.background_color = self.setting.color
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.rect = self.screen.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        pygame.display.set_caption("Aliens Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bullets2 = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        '''self._create_fleet()'''
        self.ship2 = Ship2(self)
        self.counter = 0

    def _add_bulets(self):
        if len(self.bullets2) < self.setting.num_of_bullets:
            '''
            bullet = Bullet_vert(self)
            self.bullets.add(bullet)
            '''
            bullet2 = Bullet_hroz(self)
            self.bullets2.add(bullet2)

    def _show_bullets(self):
        '''
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        '''

        for bullet2 in self.bullets2.sprites():
            bullet2.draw_bullet()
        self.bullets2.update()
        '''self.bullets.update()'''
        self.remove_old_bullets()

    def _check_for_collesions(self):
        '''
        pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)'''
        pygame.sprite.groupcollide(self.bullets2, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            '''self._create_fleet()'''
            self.setting.alien_speed += 1.0

    def remove_old_bullets(self):
        '''
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        '''
        for bullet in self.bullets2.copy():
            if bullet.rect.right > self.rect.right:
                self.bullets2.remove(bullet)

    def _check_keyDown_events(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.move_left = True
            self.ship2.move_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = True
            self.ship2.move_right = True
        elif event.key == pygame.K_UP:
            self.ship2.move_up = True
        elif event.key == pygame.K_DOWN:
            self.ship2.move_down = True
        elif event.key == pygame.K_SPACE:
            self._add_bulets()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyUp_events(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
            self.ship2.move_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = False
            self.ship2.move_right = False
        elif event.key == pygame.K_UP:
            self.ship2.move_up = False
        elif event.key == pygame.K_DOWN:
            self.ship2.move_down = False

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
        alien_height = alien.rect.height
        ship_height = self.ship.image_rect.height
        number_aliens_x = self._number_of_aliens(alien_width)
        number_rows = self._number_of_rows(alien_height, ship_height)

        for row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row)

    def _number_of_rows(self, alien_height, ship_height):
        available_space_y = (self.height
                             - (8 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        return number_rows

    def _number_of_aliens(self, alien_width):
        available_space_x = self.width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        return number_aliens_x

    def _move_fleets(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _create_alien(self, alien_number, row):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.y = alien_height + 2 * alien_height * row
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _create_alien2(self):
        if self.counter % self.setting.rate_of_aliens == 0:
            alien = Alien(self, randint(0, 1300), randint(0, 1300))
            self.aliens.add(alien)
        self.counter += 1

    def _add_alien_to_the_screen(self):
        for alien in self.aliens.sprites():
            alien.blitme()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1

    def _update_screen(self):
        self.screen.fill(self.background_color)
        '''
        self.ship.update()
        self.ship.blitme()
        '''
        self.ship2.update()
        self.ship2.blitme()
        self._show_bullets()
        self._create_alien2()
        self._add_alien_to_the_screen()
        self.aliens.update()
        '''
        self._move_fleets()
        '''
        self._check_for_collesions()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
