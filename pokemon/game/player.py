from game import constants

import arcade

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.PLAYER_IMAGE,constants.CHARACTER_SCALING)

        self.center_x = int(constants.PLAYER_START_X)
        self.center_y = int(constants.PLAYER_START_Y)