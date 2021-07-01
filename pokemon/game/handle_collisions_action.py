import random
from game import constants
from game.action import Action

import arcade

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        player = cast["player"][0]
        pokecenter = cast["pokecenter"]
        wall_hit_sound = arcade.load_sound(constants.COLLISION_SOUND)
        if arcade.check_for_collision(player,pokecenter):
            player.change_x = 0
            player.change_y = 0
            arcade.play_sound(wall_hit_sound,volume=0.05)
