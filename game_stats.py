class GameStats():
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an active state
        self.game_active = False

        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize the statistics that can change during a game."""
        self.ships_left = self.ai_settings.ship_limit  # We initialize most of the stats outside of __init__() so that
        # we can call the reset_stats() method any time the player starts a new game.
        self.score = 0
        self.level = 1

