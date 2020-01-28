"""Class for all configurations of the game"""


class Settings:

    def __init__(self):
        """Initial game configuration"""
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        """Bullet configuration"""
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Settings for alien ships
        self.fleet_drop_speed = 10
        self.ship_limit = 3

        # Increasing lvl of the game.
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings which are changing during the game"""
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.ship_speed_factor = 1.5

        # fleet_direction = 1 means moving to the right, -1 means moving to the left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increases speed settings"""
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale