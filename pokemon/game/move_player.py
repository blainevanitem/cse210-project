from game import constants
import arcade

class MovePlayer():
    def __init__(self):
        pass

    def update_location(self,key,modifiers,player_sprite):
        if key == arcade.key.UP or key == arcade.key.W:
            player_sprite.center_y += constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            player_sprite.center_y -= constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            player_sprite.center_x -= constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
             player_sprite.center_x += constants.PLAYER_MOVEMENT_SPEED