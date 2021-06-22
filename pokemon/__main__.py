import random
from game import constants
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService



from game.director import Director

import arcade

def main():
    
    # start the game
    director = Director()
    director.setup()
    arcade.run()


if __name__ == "__main__":
    main()