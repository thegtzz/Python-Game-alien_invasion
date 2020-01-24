"""Class for all configurations of the game"""


class Settings:

    def __init__(self):
        """Initial game configuration"""
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        """Bullet configuration"""
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

    ship_speed_factor = 1.5
