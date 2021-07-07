import random
from game import constants
from game.action import Action

import arcade

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        self.is_touching = False


    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        player = cast["player"][0]
        pokecenter = cast["pokecenter"]
        pokemart = cast["pokemart"]
        pokelab = cast["pokelab"]
        trees = cast["trees"]
        wall_hit_sound = arcade.load_sound(constants.COLLISION_SOUND)

        if arcade.check_for_collision(player,pokecenter):
            arcade.play_sound(wall_hit_sound,volume=0.5)
            if player.top > pokecenter.top:
                player.center_y += 5
                player.change_x = 0
                player.change_y = 0

            elif player.bottom < pokecenter.bottom:
                player.center_y -= 5
                player.change_x = 0
                player.change_y = 0

            elif player.right > pokecenter.right:
                player.center_x += 5
                player.change_x = 0
                player.change_y = 0

            elif player.left < pokecenter.left:
                player.center_x -= 5
                player.change_x = 0
                player.change_y = 0




