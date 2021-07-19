from game.point import Point
from game import constants

import arcade

class PokeTower(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = constants.BUILDING_SCALING
        self.textures = []

        texture = arcade.load_texture(constants.POKETOWER)
        self.textures.append(texture)
        
        self.texture = self.textures[0]

        self.center_x = 200
        self.center_y = 1500

        self._hit_box_algorithm = "Simple"
        points = ((-56.0, -120.0), (56.0, -120.0), (56.0, -15), (20.0, -15), (-20.0, -15), (-56.0, -15))
        self.set_hit_box(points)
        self.get_adjusted_hit_box()


