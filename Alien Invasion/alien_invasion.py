import pygame
import sys
from random import randint
from time import sleep

from setting import Settings
from bullet import Bullet_right, Bullet_left, Bullet_down, Bullet_up
from aliens import Alien
from ship2 import Ship
from game_stats import GameStats


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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.counter = 0
        self.num_of_hits = 0
        self.start = False

    def _add_bulets(self):
        if len(self.bullets) < self.setting.num_of_bullets:
            if self.ship.direction == 0:
                bullet = Bullet_up(self)
                self.bullets.add(bullet)
            elif self.ship.direction == 1:
                bullet = Bullet_right(self)
                self.bullets.add(bullet)
            elif self.ship.direction == 2:
                bullet = Bullet_down(self)
                self.bullets.add(bullet)
            else:
                bullet = Bullet_left(self)
                self.bullets.add(bullet)

    def _show_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.bullets.update()
        self.remove_old_bullets()

    def _check_for_collesions(self):
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _ship_hit(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self.ship.center_ship()
            sleep(0.5)
        if self.stats.ships_left == 0:
            self.stats.game_active = False

    def remove_old_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.right > self.rect.right:
                self.bullets.remove(bullet)
            elif bullet.rect.left < self.rect.left:
                self.bullets.remove(bullet)
            elif bullet.rect.top < self.rect.top:
                self.bullets.remove(bullet)
            elif bullet.rect.bottom > self.rect.bottom:
                self.bullets.remove(bullet)

    def _check_keyDown_events(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_UP:
            self.ship.move_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_SPACE:
            self._add_bulets()
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RETURN:
            self.stats.game_active = True
            self.start = True

    def _check_keyUp_events(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_UP:
            self.ship.move_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = False

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
        self.ship.update()
        self.ship.blitme()
        self._show_bullets()
        self._create_alien2()
        self.aliens.update()
        self._add_alien_to_the_screen()
        self._check_for_collesions()
        self._ship_hit()
        pygame.display.flip()

    def _add_text(self, message1, message2):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font('freesansbold.ttf', 64)
        text = font.render(message1, True, (255, 255, 225), (0, 0, 0))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text2 = font.render(message2, True,
                            (255, 255, 225), (0, 0, 0))
        font = pygame.font.Font('freesansbold.ttf', 20)
        text3 = font.render('PRESS (Q) TO QUIT', True,
                            (255, 255, 225), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (650, 300)
        textRect2 = text2.get_rect()
        textRect2.center = (650, 450)
        textRect3 = text2.get_rect()
        textRect3.center = (800, 600)
        self.screen.blit(text, textRect)
        self.screen.blit(text2, textRect2)
        self.screen.blit(text3, textRect3)
        pygame.display.flip()

    def _game_over(self):
        self._add_text('GAME OVER', 'PRESS ENTER TO PLAY AGAIN')

    def _game_start(self):
        self._add_text('WELCOME TO ALIENS GAME',
                       'PRESS ENTER TO START THE GAME')

    def run_game(self):
        while True:
            self._check_events()
            if not self.start:
                self._game_start()
            else:
                if self.stats.game_active:
                    self._update_screen()
                else:
                    self.stats.rest_stats()
                    self._game_over()
