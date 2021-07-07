from game.point import Point
from game import constants

import arcade

class PokeCenter(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = constants.BUILDING_SCALING
        self.textures = []

        texture = arcade.load_texture(constants.POKEMON_CENTER)
        self.textures.append(texture)
        
        self.texture = self.textures[0]

        self.center_x = constants.POKEMON_START_X
        self.center_y = constants.POKEMON_START_Y

        


