import pygame
import sys
from random import randint
from time import sleep

from setting import Settings
from bullet import Bullet_right, Bullet_left, Bullet_down, Bullet_up
from aliens import Alien
from ship2 import Ship
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


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
        self.scoreboard = ScoreBoard(self)
        self.ship = Ship(self)
        self.counter = 0
        self.counter2 = 0
        self.start = False
        self.temp1 = 0
        self.temp2 = 0
        pygame.mouse.set_visible(False)
        self.scoreboard.prep_ships()
        self.bullet_sound = pygame.mixer.Sound(r"sounds\Gun+Empty.wav")

    def _add_bulets(self):
        if len(self.bullets) < self.setting.num_of_bullets:
            pygame.mixer.Sound.play(self.bullet_sound)
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
        collision = pygame.sprite.groupcollide(self.bullets,
                                               self.aliens, True, True)
        if collision:
            self.stats.score += len(collision.keys())
            self.scoreboard.prep_score()

    def _ship_hit(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self.ship.center_ship()
            sleep(0.5)
            self.scoreboard.prep_ships()
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
            self.start = True
            self.stats.game_active = True

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
        self.scoreboard.show_score()
        pygame.display.flip()

    def _add_text(self, text, text_size, x, y, text_color, bg_color):
        font = pygame.font.Font('freesansbold.ttf', text_size)
        text = font.render(text, True, text_color, bg_color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        self.screen.blit(text, textRect)

    def _game_start(self):
        self.screen.fill((0, 0, 0))
        self._add_text('WELCOME TO ALIENS GAME', 64, 680, 300,
                       (255, 255, 225), (0, 0, 0))
        self._add_text('PRESS ( ENTER ) TO START THE GAME', 32, 700, 400,
                       (255, 255, 225), (0, 0, 0))
        self._add_text('PRESS (Q) TO QUIT', 20, 680, 500, (255, 255, 225),
                       (0, 0, 0))
        pygame.display.flip()
        self.stats.rest_stats()

    def _game_over(self):
        self.screen.fill((0, 0, 0))
        self._add_text('GAME OVER', 64, 680, 200,
                       (255, 255, 225), (0, 0, 0))
        score = str(self.stats.score)
        self._add_text('Your Score ' + score, 20, 690, 260,
                       (255, 255, 225), (0, 0, 0))
        self.stats.update_high_score()
        high_score = str(self.stats.high_score)
        self._add_text('High Score ' + high_score, 20, 690, 300,
                       (255, 255, 225), (0, 0, 0))
        self._add_text('PRESS ( ENTER ) TO PLAY AGAIN', 32, 700, 450,
                       (255, 255, 225), (0, 0, 0))
        self._add_text('PRESS (Q) TO QUIT', 20, 700, 500, (255, 255, 225),
                       (0, 0, 0))
        pygame.display.flip()
        self.aliens.empty()
        self.bullets.empty()

    def run_game(self):
        while True:
            self._check_events()
            if not self.start:
                if self.temp1 == 0:
                    self._game_start()
                    self.temp1 = 1
            else:
                if self.stats.game_active:
                    self.temp2 = 0
                    self._update_screen()
                    self.counter2 += 1
                    if self.counter2 % 2000 == 0:
                        self.setting.alien_speed += 0.2
                else:
                    if self.temp2 == 0:
                        self._game_over()
                        self.stats.rest_stats()
                        self.scoreboard.prep_score()
                        self.scoreboard.prep_ships()
                        self.temp2 += 1
