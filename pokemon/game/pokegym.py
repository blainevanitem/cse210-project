from game.point import Point
from game import constants

import arcade

class PokeGym(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = constants.BUILDING_SCALING
        self.textures = []

        texture = arcade.load_texture(constants.POKEGYM)
        self.textures.append(texture)
        
        self.texture = self.textures[0]

        self.center_x = 200
        self.center_y = 980

        self._hit_box_algorithm = "Simple"
        points = ((-48.0, -27.5), (-36.0, -39.5), (36.0, -39.5), (48.0, -27.5), (48.0, 30), (45.0, 30), (-45.0, 30), (-48.0, 30))
        self.set_hit_box(points)
        self.get_adjusted_hit_box()


