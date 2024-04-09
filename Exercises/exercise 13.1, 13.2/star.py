import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Inizialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("C:/Users/jacop/OneDrive/Desktop/Learning python/python crash course/Part 2 Alien invasion game/images/star_resized.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
