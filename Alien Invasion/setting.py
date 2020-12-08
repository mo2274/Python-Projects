
""" The settings.py fle contains the Settings class. This class only has an __init__()
method, which initializes attributes controlling the game’s appearance and
the ship’s speed
"""
class Settings():
    def __init__(self):
        self.width = 1000
        self.height = 300
        self.color = (255, 255, 255)
        self.num_of_bullets = 3
