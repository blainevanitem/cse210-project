from game.point import Point
from game import constants

import arcade

class Tree(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.scale = constants.TREE_SCALE
        self.textures = []

        texture = arcade.load_texture(constants.BIG_TREE)
        self.textures.append(texture)
        
        self.texture = self.textures[0]
        
        self.center_x = x
        self.center_y = y

        self._hit_box_algorithm = "Simple"
        points = ((-15.0, -19.0), (-11.0, -23.0), (11.0, -23.0), (15.0, -19.0), (15.0, 0.0), (2.0, 0.0), (-2.0, 0.0), (-15.0, 0.0))
        self.set_hit_box(points)
        self.get_adjusted_hit_box()



