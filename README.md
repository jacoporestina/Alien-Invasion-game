# Alien Invasion Game

Alien Invasion is a classic arcade-style game where the player controls a ship that must defend against waves of aliens. The player can move the ship left or right and shoot bullets to destroy the aliens before they reach the bottom of the screen.

## Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Create a Virtual Environment (Optional but Recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Pygame:**

    ```sh
    pip install pygame
    ```

## Running the Game

After installing Pygame, you can run the game using:

```sh
python alien_invasion.py

## How to Play

- **Start the Game:** Click the "Play" button or press `P` to start the game.
- **Move the Ship:** Use the `RIGHT` and `LEFT` arrow keys to move the ship.
- **Fire Bullets:** Press the `SPACE` bar to fire bullets at the aliens.
- **Quit the Game:** Press `Q` to quit the game.

## Game Mechanics

- The player controls a ship that can move left or right at the bottom of the screen.
- Waves of aliens move across and down the screen. The player must shoot and destroy all the aliens to advance to the next level.
- The game ends if an alien collides with the player's ship or reaches the bottom of the screen.
- The player's score increases with each alien destroyed. The game tracks and displays the high score.

## File Structure

- `alien_invasion.py`: Main game file that initializes and runs the game.
- `settings.py`: Contains settings for the game such as screen dimensions, colors, ship speed, etc.
- `ship.py`: Defines the `Ship` class representing the player's ship.
- `bullet.py`: Defines the `Bullet` class for the bullets fired by the ship.
- `alien.py`: Defines the `Alien` class for the alien enemies.
- `game_stats.py`: Manages game statistics.
- `scoreboard.py`: Manages the display of the score and high score.
- `button.py`: Manages the play button.

