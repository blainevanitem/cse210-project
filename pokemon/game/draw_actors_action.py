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
        count = 0
        try:
            arcade.draw_text("Where are my balls!?", 320, 440, arcade.color.RED,20)
            ball = cast["pokeballs"][count]
            self._output_service.draw_actor(ball)

        
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

            poketower = cast["poketower"]
            self._output_service.draw_actor(poketower)

            deptstore = cast["deptstore"]
            self._output_service.draw_actor(deptstore)

            pokegym = cast["pokegym"]
            self._output_service.draw_actor(pokegym)

            bikeshop = cast["bikeshop"]
            self._output_service.draw_actor(bikeshop)

            pokehouse1 = cast["pokehouse1"]
            for house in pokehouse1:
                self._output_service.draw_actor(house)

            littlerocks = cast["breakrock"]
            try:
                for r in littlerocks:
                    self._output_service.draw_actor(r)
            except:
                pass

        except:
            self._output_service.clear_screen()
            arcade.start_render()
            arcade.draw_text("You WIN", constants.MAX_X/2, constants.MAX_Y/2, arcade.color.AIR_FORCE_BLUE,50)
            arcade.draw_text("Professor Oak thanks you for your help!", constants.MAX_X/2-250, constants.MAX_Y/2-150, arcade.color.BLUEBERRY,30)


        
        


        self._output_service.flush_buffer()

