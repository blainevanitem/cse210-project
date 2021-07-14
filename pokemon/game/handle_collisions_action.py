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
        treesides = cast["treesides"]
        rocks = cast["bigrocks"]
        fountains = cast["fountains"]
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

        for treesides in treesides:
            if arcade.check_for_collision(player,treesides):
                arcade.play_sound(wall_hit_sound,volume=0.5)
                if player.top > treesides.top:
                    player.center_y += 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.bottom < treesides.bottom:
                    player.center_y -= 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.right > treesides.right:
                    player.center_x += 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.left < treesides.left:
                    player.center_x -= 5
                    player.change_x = 0
                    player.change_y = 0


        if arcade.check_for_collision(player,pokemart):
            arcade.play_sound(wall_hit_sound,volume=0.5)
            if player.top > pokemart.top:
                player.center_y += 5
                player.change_x = 0
                player.change_y = 0

            elif player.bottom < pokemart.bottom:
                player.center_y -= 5
                player.change_x = 0
                player.change_y = 0

            elif player.right > pokemart.right:
                player.center_x += 5
                player.change_x = 0
                player.change_y = 0

            elif player.left < pokemart.left:
                player.center_x -= 5
                player.change_x = 0
                player.change_y = 0


        if arcade.check_for_collision(player,pokelab):
            arcade.play_sound(wall_hit_sound,volume=0.5)
            if player.top > pokelab.top:
                player.center_y += 5
                player.change_x = 0
                player.change_y = 0

            elif player.bottom < pokelab.bottom:
                player.center_y -= 5
                player.change_x = 0
                player.change_y = 0

            elif player.right > pokelab.right:
                player.center_x += 5
                player.change_x = 0
                player.change_y = 0

            elif player.left < pokelab.left:
                player.center_x -= 5
                player.change_x = 0
                player.change_y = 0

        for tree in trees:
            if arcade.check_for_collision(player,tree):
                
                arcade.play_sound(wall_hit_sound,volume=0.5)
                if player.top > tree.top:
                    player.center_y += 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.bottom < tree.bottom:
                    player.center_y -= 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.right > tree.right:
                    player.center_x += 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.left < tree.left:
                    player.center_x -= 5
                    player.change_x = 0
                    player.change_y = 0

        for rock in rocks:
            if arcade.check_for_collision(player,rock):
                arcade.play_sound(wall_hit_sound,volume=0.5)
                if player.top > rock.top:
                    player.center_y += 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.bottom < rock.bottom:
                    player.center_y -= 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.right > rock.right:
                    player.center_x += 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.left < rock.left:
                    player.center_x -= 5
                    player.change_x = 0
                    player.change_y = 0
            
        for fountain in fountains:
            if arcade.check_for_collision(player,fountain):
                arcade.play_sound(wall_hit_sound,volume=0.5)
                if player.top > fountain.top:
                    player.center_y += 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.bottom < fountain.bottom:
                    player.center_y -= 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.right > fountain.right:
                    player.center_x += 5
                    player.change_x = 0
                    player.change_y = 0

                elif player.left < fountain.left:
                    player.center_x -= 5
                    player.change_x = 0
                    player.change_y = 0
            
        