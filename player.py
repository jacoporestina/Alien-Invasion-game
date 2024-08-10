import pygame
from pygame import mixer

class Player:
    """Manage music and sounds."""

    def __init__(self):
        """Initialize music and sounds"""
        pygame.mixer.init()
        self.explosion_sound = mixer.Sound("sounds/explosion-91872.mp3")
        self.laser_sound = mixer.Sound("sounds/laser-104024.mp3")
        self.game_over_sound = mixer.Sound("sounds/game-over-39-199830.mp3")

    def play_music(self):
        """handle background music features."""
        mixer.music.load("music/space-invaders-classic-arcade-game-116826.mp3")
        mixer.music.set_volume(1)  # Set the volume (0.0 to 1.0)
        mixer.music.play(-1)  # Play the music indefinitely (-1 loop)

    def explosion(self):
        """handle explosion sound."""
        self.explosion_sound.set_volume(1)
        self.explosion_sound.play()

    def laser(self):
        """handle laser sound."""
        self.laser_sound.set_volume(1)
        self.laser_sound.play()
        
    def game_over(self):
        """handle game over sound."""
        self.game_over_sound.set_volume(1)
        self.game_over_sound.play()