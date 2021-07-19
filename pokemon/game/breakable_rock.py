from game.point import Point
from game import constants

import arcade

class BreakRock(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.scale = constants.BREAK_ROCK_SCALE
        self.textures = []

        texture = arcade.load_texture(constants.BREAK_ROCK)
        self.textures.append(texture)
        
        self.texture = self.textures[0]
        
        self.center_x = x
        self.center_y = y



