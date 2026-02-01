class Settings():
    """A class to store all the settings for Alien Invasion."""
    def __init__(self):
        """Initialise the game's static settings."""
        self.screen_width = 1150
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # Alien settings.
        self.fleet_drop_speed = 20

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # Fleet direction of 1 represents moving right; -1 represents moving left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50


    def increase_speed(self):
        """Increase the speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = self.alien_points * self.score_scale

