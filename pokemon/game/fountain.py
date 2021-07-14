from game.point import Point
from game import constants

import arcade
import time

class Fountain(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.scale = constants.BUILDING_SCALING
        self.textures = []
        self.texture_number = 0

        texture = arcade.load_texture(constants.FOUNTAIN1)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN1)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN1)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN2)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN2)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN2)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN3)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN3)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN3)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN4)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN4)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN4)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN5)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN5)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.FOUNTAIN5)
        self.textures.append(texture)
         
        self.texture = self.textures[self.texture_number]

        self.center_x = x
        self.center_y = y

        
    def update(self):
        if self.texture_number == 15:
            self.texture_number = 0
        self.texture = self.textures[self.texture_number]
        
        self.texture_number += 1

        