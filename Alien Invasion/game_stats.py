
class GameStats(object):
    def __init__(self, ai_game):
        self.setting = ai_game.setting
        self.game_active = False
        self.high_score = 0
        self.score = 0
        self.rest_stats()

    def rest_stats(self):
        self.ships_left = self.setting.ships_limit
        self.setting.alien_speed = 0.5
        self.score = 0

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
