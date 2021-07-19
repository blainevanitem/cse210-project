from game.point import Point
from game import constants

import arcade

class BikeShop(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = constants.BUILDING_SCALING
        self.textures = []

        texture = arcade.load_texture(constants.BIKESHOP)
        self.textures.append(texture)
        
        self.texture = self.textures[0]

        self.center_x = 600
        self.center_y = 1300

        self._hit_box_algorithm = "Simple"
        points = ((-32.0, -41.0), (-27.0, -46.0), (27.0, -46.0), (32.0, -41.0), (32.0, 38), (28.0, 38), (-28.0, 38), (-32.0, 38))
        self.set_hit_box(points)
        self.get_adjusted_hit_box()


