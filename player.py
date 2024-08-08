import pygame
from pygame import mixer

class Player:
    """Manage music and sounds."""

    def __init__(self):
        """Initialize music and sounds"""
        self.game_music = mixer.Sound("C:/Users/jacop/OneDrive/Desktop/Learning python/python crash course/alien_invasion_game/music/space-invaders-classic-arcade-game-116826.mp3")
        self.explosion_sound = mixer.Sound("C:/Users/jacop/OneDrive/Desktop/Learning python/python crash course/alien_invasion_game/sounds/explosion-91872.mp3")
        self.laser_sound = mixer.Sound("C:/Users/jacop/OneDrive/Desktop/Learning python/python crash course/alien_invasion_game/sounds/laser-104024.mp3")
        #self.game_over_music = mixer.Sound()

    def play_music(self):
        """handle background music features."""
        self.game_music.set_volume(0.2)  # Set the volume (0.0 to 1.0)
        self.game_music.play(-1)  # Play the music indefinitely (-1 loop)

    def game_over(self):
        """handle game over music."""
        self.game_music.stop()
        self.game_over_music.play()

    def explosion(self):
        """handle explosion sound."""
        self.explosion_sound.set_volume(1)
        self.explosion_sound.play()

    def laser(self):
        """handle laser sound."""
        self.laser_sound.set_volume(1)
        self.laser_sound.play()
        print("Laser sound should play now") # Debugging