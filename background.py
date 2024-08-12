import pygame

class Background:
    """Class that manages background features and movement of the game."""

    def __init__(self, ai_game):
        """Initialize background characteristics."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.background_image = pygame.image.load("images/space_background.png")
        self.background_rect = self.background_image.get_rect()
        self.scroll_speed = 2
        self.background_rect.y = 0

    def update_background(self):
        """Movement of the background."""
        # Move the background downwards the screen
        self.background_rect.y += self.scroll_speed

        # Reset the bacbground postion when it reached the bottom of the screen
        if self.background_rect.y >= self.background_rect.height:
            self.background_rect.y = 0

    def draw_background(self):
        """Draw background on the screen."""
        self.screen.blit(self.background_image, (0, self.background_rect.y - self.background_rect.height))
        self.screen.blit(self.background_image, (0, self.background_rect.y))


   
