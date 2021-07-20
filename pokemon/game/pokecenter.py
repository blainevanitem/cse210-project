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
        texture = arcade.load_texture(constants.POKECENTERDOOR1)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.POKECENTERDOOR1)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.POKECENTERDOOR1)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.POKECENTERDOOR2)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.POKECENTERDOOR2)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.POKECENTERDOOR2)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.POKECENTERDOOR3)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.POKECENTERDOOR3)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.POKECENTERDOOR3)
        self.textures.append(texture)
        
        self.texture = self.textures[0]

        self.center_x = constants.POKEMON_START_X
        self.center_y = constants.POKEMON_START_Y

        # self._hit_box_algorithm = "Simple"
        # points = ((-40.0, -27.0), (-32.0, -35.0), (32.0, -35.0), (40.0, -27.0), (40.0, 26.0), (35.0, 26.0), (-35.0, 26.0), (-40.0, 26.0))
        # self.set_hit_box(points)
        # self.get_adjusted_hit_box()

        self.counter = 0
        self.reverse = False
        

    def execute(self):
        if self.counter == 9:
            self.reverse = True
        else:
            self.counter += 1

        if self.reverse == True:
            self.counter -=1

        if self.counter == 0:
            self.reverse = False
        
        self.texture = self.textures[self.counter]
