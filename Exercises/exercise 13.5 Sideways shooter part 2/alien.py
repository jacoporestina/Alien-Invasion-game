import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to manage the alien."""

    def __init__(self, ai_game):
        """Inizialize alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
    
        # Upload a picture of a alien and get its rect
        self.alien_image = pygame.image.load("C:/Users/jacop/OneDrive/Desktop/Learning python/python crash course/alien_invasion_game/images/alien_resized.bmp")
        self.image = pygame.transform.rotate(self.alien_image, -90)
        self.rect = self.image.get_rect()

        # Define position to place the alien
        self.rect.x = self.screen_rect.width - (2 * self.rect.width) 
        self.rect.y = self.rect.height

        # Define the horizontal and vertical position of the alien
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update aliens movements to the left and right."""
        self.y -= (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y

    def check_edges(self):
        """Check if the fleet hit edges. In case, change direction."""
        if self.rect.top <= 0  or self.rect.bottom >= self.screen_rect.bottom:
            return True

