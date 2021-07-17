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
        points = ((-195.0, -30.5), (-191.0, -34.5), (191.0, -34.5), (195.0, -30.5), (195.0, 21.5), (182.0, 21.5), (-182.0, 21.5), (-195.0, 21.5))
        self.set_hit_box(points)
        self.get_adjusted_hit_box()




