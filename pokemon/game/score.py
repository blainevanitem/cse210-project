import random
from game import constants
from game.action import Action

import arcade

class HandleCollectionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        #self._output_service = output_service
        self.score = 0
        pass


    def execute(self, cast, director):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        player = cast["player"][0]
        pokeballs = cast["pokeballs"]
        collection = False
        
    
        wall_hit_sound = arcade.load_sound(constants.COLLISION_SOUND)


        for balls in pokeballs:
            if arcade.check_for_collision(player, balls):
                collection = True 

                if player.top > balls.top:
                    player.center_y += 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.bottom < balls.bottom:
                    player.center_y -= 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.right > balls.right:
                    player.center_x += 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.left < balls.left:
                    player.center_x -= 5
                    player.change_x = 0
                    player.change_y = 0
                self.score += 1
                print(self.score)
                count = 0
                del cast["pokeballs"][count]
                count+=1

            return self.score
                             
                
                    



    