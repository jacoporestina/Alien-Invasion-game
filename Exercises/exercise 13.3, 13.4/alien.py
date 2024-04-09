import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Inizialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("C:/Users/jacop/OneDrive/Desktop/Learning python/python crash course/alien_invasion_game/images/raindrop_resized.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact vertical and horizontal position.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
    
    def update(self):
        """Move the raindrop to the bottom."""
        self.y += self.settings.alien_speed
        self.rect.y = self.y