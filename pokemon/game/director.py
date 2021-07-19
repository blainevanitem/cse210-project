import arcade
from game import constants

class Director(arcade.Window):
    def __init__(self, cast, script, input_service):
        """Initialize the game
        """
        super().__init__(constants.MAX_X, constants.MAX_Y, constants.SCREEN_TITLE)
        self._cast = cast
        self._script = script
        self._input_service = input_service

        self.score = 0
        self.fountain = cast["fountains"]
        self.view_bottom = 0
        self.view_left = 0
        self.player_sprite = cast["player"][0]


    def setup(self):
        arcade.set_background_color(arcade.color.WHEAT)     

    def on_update(self, delta_time):

        self.score = self._cue_action("update")
        self._cue_action("update")
        for fountain in self.fountain:
            fountain.update()

        changed = False
        
        # Scroll up
        top_boundary = self.view_bottom + constants.MAX_Y - constants.TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + constants.BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                constants.MAX_X + self.view_left,
                                self.view_bottom,
                                constants.MAX_Y + self.view_bottom)
        


    def on_draw(self):
        self._cue_action("output")

    def on_key_press(self, symbol, modifiers):
        self._input_service.set_key(symbol, modifiers)
        self._cue_action("input")

    def on_key_release(self, symbol, modifiers):
        self._input_service.remove_key(symbol, modifiers)
        self._cue_action("input")

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)

