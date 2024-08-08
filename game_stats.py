class GameStats:
    """Track statistics of alien invasion game."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # High score should never be reset.
        self.high_score_file = "highest_score.txt"
        self.high_score = self.read_high_score()

    def read_high_score(self):
        """Read highest score in the file."""
        try:
            with open(self.high_score_file, 'r') as file:
                return int(file.read().strip())
        
        except FileNotFoundError:
            return 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit 
        self.score = 0
        self.level = 1
        
