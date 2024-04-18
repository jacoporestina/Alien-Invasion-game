import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from target import Target

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

        # create an instance to store game statistics
        self.stats = GameStats(self)

        # Create an instance of the ship
        self.ship = Ship(self)

        # Create instance and sprites of bullets
        self.bullets = pygame.sprite.Group()

        # Creat an instance of the target
        self.target = Target(self )

        # Make the play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()
                
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Start a new game every time Play is pressed"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset game statistics
            self.stats.reset_stats()
            self.stats.game_active = True

            # Get rid of any remaining bullets
            self.bullets.empty()

            # Center ship and replace target
            self.ship.center_ship()
            self.target.place_target()

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
                # When a bullet reaches the screen, is removed and bullet_counter decreases
                self.bullets.remove(bullet)
                self.stats.bullet_counter -= 1
        self._bullet_finished()

        self._check_target_bullet_collision()

    def _check_target_bullet_collision(self):
        """Check if bullets hit target"""
        collisions = pygame.sprite.spritecollide(self.target, self.bullets, True)

    def _bullet_finished(self):
        """Manage to restart the game when bullets are finished"""
        if self.stats.bullet_counter == 0:
            self.stats.game_active = False

    def _check_target_edges(self):
        """Respond appropriately when the target reach the edges."""
        if self.target.check_edges():
            self._change_target_direction()

    def _change_target_direction(self):
        """Change direction of target"""
        self.settings.target_direction *= -1

    def _update_target(self):
        """Check if target hit the edges, then update target movement in the game."""
        self._check_target_edges()
        self.target.update()

    def _update_screen(self):
        """Update imgages on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw the target 
        self.target.draw_target()

        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()