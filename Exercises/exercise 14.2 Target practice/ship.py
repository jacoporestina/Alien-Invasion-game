import pygame

class Ship:
    """A class that manages the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.raw_image = pygame.image.load("C:/Users/jacop/OneDrive/Desktop/Learning python/python crash course/alien_invasion_game/images/ship.bmp")
        self.image = pygame.transform.rotate(self.raw_image, -90)
        self.rect = self.image.get_rect()

        # Start each new ship at the left center of the screen.
        self.rect.midleft = self.screen_rect.midleft
        
        # Store a decimal value for the ship's vertical position.
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the ship's position based on movement flags"""
        # Update the ship's y value, not the rect
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # Move the ship to the bottom, so increase y (within screen's limits)
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            # Move the ship to the top, so decrease y (within screen's limits)
            self.y -= self.settings.ship_speed

        # Update rect object from self.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Center new ship"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = self.rect.y
        
        
        