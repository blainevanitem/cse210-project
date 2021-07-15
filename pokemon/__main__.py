import random
from game import constants
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService

from game.player import Player
from game.pokecenter import PokeCenter
from game.pokemart import PokeMart
from game.director import Director
from game.pokelab import PokeLab
from game.tree import Tree
from game.bigrock import BigRock
from game.pokeball import PokeBall
from game.treesides import TreeSides

import arcade

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    player = Player()
    cast["player"] = [player]
    pokecenter = PokeCenter()
    cast["pokecenter"] = pokecenter
    pokemart = PokeMart()
    cast["pokemart"] = pokemart
    pokelab = PokeLab()
    cast["pokelab"] = pokelab
    
    cast["bigrocks"] = []
    cast["trees"] = []
    cast["pokeballs"] = []
    cast["treesides"] = []

    ball = PokeBall(80,80) #Bottom Left
    cast["pokeballs"].append(ball)
    ball = PokeBall(730,650) #Top Right rocks
    cast["pokeballs"].append(ball)
    ball = PokeBall(500,420)
    cast["pokeballs"].append(ball)
    # ball = PokeBall(100,700)
    # cast["pokeballs"].append(ball)
    # ball = PokeBall(700,100)
    # cast["pokeballs"].append(ball)
    # ball = PokeBall(80, 850)
    # cast["pokeballs"].append(ball)

    for x in range(5,350,45):
        tree = Tree(x,800)
        cast["trees"].append(tree)

    for x in range(5,350,45):
        tree = Tree(x,760)
        cast["trees"].append(tree)

    
    lefttreeside = TreeSides(4,400)
    cast["treesides"].append(lefttreeside)

    lefttreeside = TreeSides(49,400)
    cast["treesides"].append(lefttreeside)

    lefttreeside = TreeSides(814,92)
    cast["treesides"].append(lefttreeside)

    lefttreeside = TreeSides(769,92)
    cast["treesides"].append(lefttreeside)



    for x in range(470,840,45):
        tree = Tree(x,800)
        cast["trees"].append(tree)

    for x in range(470,840,45):
        tree = Tree(x,760)
        cast["trees"].append(tree)

    # for y in range(600,0,-45):
    #     tree = Tree(810,y)
    #     cast["trees"].append(tree)
    
    # for y in range(600,0,-45):
    #     tree = Tree(770,y)
    #     cast["trees"].append(tree)

    for x in range(4,850,45):
        tree = Tree(x,40)
        cast["trees"].append(tree)

    for x in range(4,850,45):
        tree = Tree(x,5)
        cast["trees"].append(tree)
    
    # for y in range(850,-50,-45):
    #     tree = Tree(4,y)
    #     cast["trees"].append(tree)

    # for y in range(850,-50,-45):
    #     tree = Tree(48,y)
    #     cast["trees"].append(tree)

    for x in range(800,650,-69):
        rock = BigRock(x,700)
        cast["bigrocks"].append(rock)
    
    
    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]
    
    # start the game
    director = Director(cast, script, input_service)
    director.setup()
    starter_music = arcade.load_sound(constants.STARTER_MUSIC)
    arcade.play_sound(starter_music,looping=True, volume=0.05)
    arcade.run()


if __name__ == "__main__":
    main()