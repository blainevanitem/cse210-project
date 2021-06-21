import random
from game import constants
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService

from game.director import Director
from game.player import Player
import arcade

def main():
    cast = {}

    player = Player()
    cast["player"] = [player]

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()

    script = {}
    script["input"] = [input_service]
    script["output"] = [output_service]

    # start the game
    director = Director(cast, script, input_service)
    director.setup()
    arcade.run()


if __name__ == "__main__":
    main()