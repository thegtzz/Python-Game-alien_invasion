class GameStats():
    """Tracks a statistics for Alien Invasion game"""

    def __init__(self, ai_settings):
        """Initializes a statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """Initializes a statistics, which changes during the game"""
        self.ships_left = self.ai_settings.ship_limit
