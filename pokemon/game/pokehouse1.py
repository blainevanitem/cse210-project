from game.point import Point
from game import constants

import arcade

class PokeHouse1(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.scale = constants.BUILDING_SCALING
        self.textures = []

        texture = arcade.load_texture(constants.POKEHOUSE1)
        self.textures.append(texture)
        
        self.texture = self.textures[0]

        self.center_x = x
        self.center_y = y

        # self._hit_box_algorithm = "Simple"
        # points = ((-56.0, -120.0), (56.0, -120.0), (56.0, -15), (20.0, -15), (-20.0, -15), (-56.0, -15))
        # self.set_hit_box(points)
        # self.get_adjusted_hit_box()


