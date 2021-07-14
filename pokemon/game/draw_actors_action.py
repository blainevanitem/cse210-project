from game.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            _output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service
        self.texturenumber = 0

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()

        player = cast["player"][0] # there's only one
        self._output_service.draw_actor(player)
        
        fountains = cast["fountains"]
        for fountain in fountains:
            self._output_service.draw_actor(fountain)

        pokecenter = cast["pokecenter"]
        self._output_service.draw_actor(pokecenter)
        

        pokemart = cast["pokemart"]
        self._output_service.draw_actor(pokemart)

        pokelab = cast["pokelab"]
        self._output_service.draw_actor(pokelab)

        

        trees = cast["trees"]
        for tree in trees:
            self._output_service.draw_actor(tree)

        rocks = cast["bigrocks"]
        for rock in rocks:
            self._output_service.draw_actor(rock)

        sidetrees = cast["treesides"]
        for tree in sidetrees:
            self._output_service.draw_actor(tree)

        count = 0
        try:
            ball = cast["pokeballs"][count]
            self._output_service.draw_actor(ball)

        except:
            self._output_service.clear_screen()
            arcade.start_render()
            arcade.draw_text("You WIN", constants.MAX_X/2, constants.MAX_Y/2, arcade.color.AIR_FORCE_BLUE)

        
        


        self._output_service.flush_buffer()

