class Settings:
    """A class to store all the settings of the alien invasion game."""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 1

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.bullet_limit = 3

        # Target settings
        self.target_speed = 0.1
        self.target_direction = 1
        
