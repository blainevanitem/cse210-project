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
        wall_hit_sound = arcade.load_sound(constants.COLLISION_SOUND)


        if arcade.check_for_collision(player,pokecenter) and self.is_touching == False:
            player.change_x = 0
            player.change_y = 0
            arcade.play_sound(wall_hit_sound,volume=0.05)
            self.is_touching = True

        elif arcade.check_for_collision(player,pokecenter) == False and self.is_touching == True:
            arcade.play_sound(wall_hit_sound,volume=0.05)
            self.is_touching = False
        
        if arcade.check_for_collision(player,pokemart) and self.is_touching == False:
            player.change_x = 0
            player.change_y = 0
            arcade.play_sound(wall_hit_sound,volume=0.05)
            self.is_touching = True

        
        if arcade.check_for_collision(player,pokelab) and self.is_touching == False:
            player.change_x = 0
            player.change_y = 0
            arcade.play_sound(wall_hit_sound,volume=0.05)
            self.is_touching = True




