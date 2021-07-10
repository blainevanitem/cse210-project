from game.point import Point
from game import constants

import arcade

class PokeLab(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = constants.BUILDING_SCALING
        self.textures = []

        texture = arcade.load_texture(constants.POKEMON_LAB)
        self.textures.append(texture)
        
        self.texture = self.textures[0]

        self.center_x = constants.POKELAB_START_X
        self.center_y = constants.POKELAB_START_Y

        self._hit_box_algorithm = "Simple"
        points = ((-56.0, -35.0), (-55.0, -36.0), (55.0, -36.0), (56.0, -35.0), (56.0, 31.0), (55.0, 31.0), (-55.0, 31.0), (-56.0, 31.0))
        self.set_hit_box(points)
        self.get_adjusted_hit_box()


