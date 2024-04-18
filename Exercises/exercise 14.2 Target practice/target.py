import pygame

class Target:
    """A Class to manage the target."""

    def __init__(self, ai_game):
        """Define the target and its properties"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Set the size and characteristics of the target
        self.width, self.height = 20, 100
        self.button_color = (255, 0, 0)

        # Build target rect object and define position of target
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midright = self.screen_rect.midright

        # Store a decimal value for the target's vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Update target movement and change direction"""
        self.y -= (self.settings.target_speed * self.settings.target_direction)
        self.rect.y = self.y

    def check_edges(self):
        """Check if the target hit edges. In case, change direction."""
        if self.rect.top <= 0  or self.rect.bottom >= self.screen_rect.bottom:
            return True

    def draw_target(self):
        """Draw blank button"""
        self.screen.fill(self.button_color, self.rect)

    def place_target(self):
        """Replace new target"""
        self.rect.midright = self.screen_rect.midright
        self.y = self.rect.y

