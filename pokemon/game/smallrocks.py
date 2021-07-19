import random
from game import constants
from game.action import Action
from game.breakable_rock import BreakRock

import arcade

class HandleBreaksAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        #self._output_service = output_service
        self.score = 0
        pass


    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        player = cast["player"][0]
        smallrocks = cast["breakrock"]
        
    
        wall_hit_sound = arcade.load_sound(constants.COLLISION_SOUND)

        #collisions
        for rock in smallrocks:

            # if arcade.check_for_collision(player, rock):
            #     print( f"x={player.center_x}")
            #     print( f"y={player.center_y}")

            #     if player.top > rock.top:
            #         player.center_y += 5
            #         player.change_x = 0
            #         player.change_y = 0

            #     elif player.bottom < rock.bottom:
            #         player.center_y -= 5
            #         player.change_x = 0
            #         player.change_y = 0

            #     elif player.right > rock.right:
            #         player.center_x += 5
            #         player.change_x = 0
            #         player.change_y = 0

            #     elif player.left < rock.left:
            #         player.center_x -= 5
            #         player.change_x = 0
            #         player.change_y = 0
            off_screen = littlerock = BreakRock(1000,100)
            
            if arcade.check_for_collision(player, rock) and ((player.center_x < 665 and player.center_x > 625) and (player.center_y < 120 and player.center_y > 70)):
              
                indexer = len(smallrocks)
                spot = 0
                cast["breakrock"].pop(spot)
                cast["breakrock"].insert(spot,off_screen) 
              
            
            if arcade.check_for_collision(player, rock) and (player.center_x < 340 and player.center_x > 310) and (player.center_y < 820 and player.center_y >750):
                try:
                    
                    spot = 1
                    cast["breakrock"].pop(spot)
                    cast["breakrock"].insert(spot,off_screen)
                except:
                    pass
            
            if arcade.check_for_collision(player, rock) and (player.center_x < 380 and player.center_x > 320 and (player.center_y < 820 and player.center_y >750)):
                try:
                    
                    spot = 2
                    cast["breakrock"].pop(spot)
                    cast["breakrock"].insert(spot, off_screen)
                except:
                    pass

            if arcade.check_for_collision(player, rock) and (player.center_x < 410 and player.center_x > 360 and (player.center_y < 820 and player.center_y >750)):
                try:
                    
                    spot = 3
                    cast["breakrock"].pop(spot)
                    cast["breakrock"].insert(spot, off_screen)
                except:
                    pass
                             
                
                    



    