from game.point import Point
from game import constants

import arcade

class PokeMart(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = constants.BUILDING_SCALING
        self.textures = []

        texture = arcade.load_texture(constants.POKEMON_MARKET)
        self.textures.append(texture)
        
        self.texture = self.textures[0]

        self.center_x = constants.POKEMART_START_X
        self.center_y = constants.POKEMART_START_Y

        self._hit_box_algorithm = "Simple"
        points = ((-32.0, -23.0), (-24.0, -31.0), (24.0, -31.0), (32.0, -23.0), (32.0, 22.0), (27.0, 22.0), (-27.0, 22.0), (-32.0, 22.0))
        self.set_hit_box(points)
        self.get_adjusted_hit_box()


