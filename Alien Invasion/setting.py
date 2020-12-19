
""" The settings.py fle contains the Settings class.
    This class only has an __init__()
method, which initializes attributes controlling the game’s appearance and
the ship’s speed
"""


class Settings():
    def __init__(self):
        self.width = 1000
        self.height = 300
        self.color = (255, 255, 255)
        self.num_of_bullets = 10
        self.bullet_speed = 5
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.rate_of_aliens = 200
        self.ships_limit = 5
