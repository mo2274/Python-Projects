
class GameStats(object):
    def __init__(self, ai_game):
        self.setting = ai_game.setting
        self.game_active = True
        self.rest_stats()

    def rest_stats(self):
        self.ships_left = self.setting.ships_limit
