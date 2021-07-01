import random
from game import constants
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService

from game.player import Player
from game.pokecenter import PokeCenter
from game.pokemart import PokeMart
from game.director import Director
from game.pokelab import PokeLab
import arcade

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    player = Player()
    cast["player"] = [player]
    pokecenter = PokeCenter()
    cast["pokecenter"] = pokecenter
    pokemart = PokeMart()
    cast["pokemart"] = pokemart
    pokelab = PokeLab()
    cast["pokelab"] = pokelab
    
    
    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script, input_service)
    director.setup()
    starter_music = arcade.load_sound(constants.STARTER_MUSIC)
    arcade.play_sound(starter_music,looping=True, volume=0.05)
    arcade.run()


if __name__ == "__main__":
    main()