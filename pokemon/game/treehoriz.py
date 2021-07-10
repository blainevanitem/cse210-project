from game.point import Point
from game import constants

import arcade

class TreeHoriz(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.scale = constants.TREE_SCALE
        self.textures = []

        texture = arcade.load_texture(constants.TREE_HORIZ)
        self.textures.append(texture)
        
        self.texture = self.textures[0]
        
        self.center_x = x
        self.center_y = y

        self._hit_box_algorithm = "None"




