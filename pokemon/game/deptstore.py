from game.point import Point
from game import constants

import arcade

class DeptStore(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = constants.BUILDING_SCALING
        self.textures = []

        texture = arcade.load_texture(constants.DEPTBUILDING)
        self.textures.append(texture)
        
        self.texture = self.textures[0]

        self.center_x = 545
        self.center_y = 2000

        self._hit_box_algorithm = "Simple"
        points = ((-71.0, -71.5), (-60.0, -82.5), (60.0, -82.5), (71.0, -71.5), (71.0, 50), (66.0, 50), (-66.0, 50), (-71.0, 50))
        self.set_hit_box(points)
        self.get_adjusted_hit_box()


