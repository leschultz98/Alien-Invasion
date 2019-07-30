class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Ship settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_height = 10
        self.bullet_color = 200, 200, 200
        self.bullets_allowed = 3

        # Alien settings.
        self.fleet_drop_speed = 20

        # How quickly the game speeds up and the alien point values increase.
        self.speedup_scale = 1.5
        self.bullet_scale = 2
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 3.5
        self.bullet_width = 2
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 2.1

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring.
        self.alien_points = 10

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        if self.bullet_width < 500:
            self.bullet_width *= self.bullet_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
