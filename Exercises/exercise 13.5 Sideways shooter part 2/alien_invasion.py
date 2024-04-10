import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """initialaze game and create gaem resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_alien()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
    
    def fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Creat a fleet of aliens."""
        # Define alien.
        alien = Alien(self)

        # Define available space and how many aliens fit in a row.
        alien_height, alien_width = alien.rect.size
        available_space_y = self.settings.screen_height - (2 * alien_height)
        number_aliens_y = available_space_y // (2 * alien_height) 
        
        # Define how many rows of aliens fit in the screen.
        available_space_x = self.settings.screen_width -  (4 * alien_width) - self.ship.rect.width
        number_rows_x = available_space_x // (2 * alien_width)

        # Create fleet of aliens.
        for row_number in range(number_rows_x):
            for alien_number in range(number_aliens_y):
                # Create a new instance of an alien.
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Method to manage the creation of a single alien"""
        # Define alien.
        alien = Alien(self)

        # Define alien height and width, then alien position.
        alien_height, alien_width = alien.rect.size
        alien.rect.y = alien_height + (2 * alien_height) * alien_number
        alien.rect.x = self.settings.screen_width - (alien_width + (2 * alien_width) * row_number)

        # Add alien to the group.
        self.aliens.add(alien)

    def _change_alien_fleet_direction(self):
        """Change direction of alien fleet and drop entire fleet"""
        self.aliens.check_edges()

    def _update_alien(self):
        """Update alien movement in the game."""
        self.aliens.update()

    def _update_screen(self):
        """Update imgages on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()