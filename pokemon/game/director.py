import arcade
from game import constants
from game.player import Player
from game.move_player import MovePlayer

class Director(arcade.Window):
    def __init__(self):
        """Initialize the game
        """
        super().__init__(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,constants.SCREEN_TITLE)
        self.move_player = MovePlayer()
        self.npc_list = None
        self.wall_list = None
        self.player_list = None

        self.player_sprite = None

    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.npc_list = arcade.SpriteList(use_spatial_hash=True)
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.player_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite(constants.PLAYER_IMAGE, constants.CHARACTER_SCALING)
        self.player_sprite.center_x = constants.PLAYER_START_X
        self.player_sprite.center_y = constants.PLAYER_START_Y
        self.player_list.append(self.player_sprite)



    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        # Code to draw the screen goes here
        self.player_sprite.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        self.move_player.update_location(key,modifiers,self.player_sprite)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
 
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.center_y += 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.center_y -= 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.center_x -= 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.center_x += 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        