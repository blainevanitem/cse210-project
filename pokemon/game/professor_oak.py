from game.point import Point
from game import constants

import arcade

class Professor(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = .8
        self.textures = []

        texture = arcade.load_texture(constants.PROFESSOR)
        self.textures.append(texture)
        
        self.texture = self.textures[0]

        self.center_x = 340
        self.center_y = 495

        # self._hit_box_algorithm = "Simple"
        # points = ((-56.0, -35.0), (-55.0, -36.0), (55.0, -36.0), (56.0, -35.0), (56.0, 31.0), (55.0, 31.0), (-55.0, 31.0), (-56.0, 31.0))
        # self.set_hit_box(points)
        # self.get_adjusted_hit_box()


