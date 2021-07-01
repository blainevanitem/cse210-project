from game.point import Point
from game import constants

import arcade

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = constants.CHARACTER_SCALING
        self.textures = []

        texture = arcade.load_texture(constants.PLAYER_IMAGE)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.PLAYER_BACK)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.PLAYER_RIGHT)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.PLAYER_LEFT)
        self.textures.append(texture)



        self.texture = self.textures[0]

        self.center_x = int(constants.MAX_X / 2)
        self.center_y = int(constants.MAX_Y / 2)

        