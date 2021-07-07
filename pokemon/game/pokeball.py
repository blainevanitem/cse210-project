from game.point import Point
from game import constants

import arcade

class PokeBall(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.scale = 1.7
        self.textures = []

        texture = arcade.load_texture(constants.POKEBALL)
        self.textures.append(texture)
        
        self.texture = self.textures[0]
        
        self.center_x = x
        self.center_y = y



