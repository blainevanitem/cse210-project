import random
from game import constants
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService
from game.score import HandleCollectionsAction
from game.smallrocks import HandleBreaksAction

from game.player import Player
from game.pokecenter import PokeCenter
from game.pokemart import PokeMart
from game.director import Director
from game.pokelab import PokeLab
from game.tree import Tree
from game.bigrock import BigRock
from game.pokeball import PokeBall
from game.treesides import TreeSides
from game.treehoriz import TreeHoriz
from game.fountain import Fountain
from game.breakable_rock import BreakRock
from game.poketower import PokeTower
from game.deptstore import DeptStore
from game.pokegym import PokeGym
from game.bikeshop import BikeShop
from game.pokehouse1 import PokeHouse1
from game.professor_oak import Professor

import arcade

def main():

    cast = {}

    player = Player()
    cast["player"] = [player]
    pokecenter = PokeCenter()
    cast["pokecenter"] = pokecenter
    pokemart = PokeMart()
    cast["pokemart"] = pokemart
    pokelab = PokeLab()
    cast["pokelab"] = pokelab
    prof = Professor()
    cast['professor'] = prof
    
    
    cast["bigrocks"] = []
    cast["trees"] = []
    cast["pokeballs"] = []
    cast["treesides"] = []
    cast["fountains"] = []
    cast["breakrock"] = []
    cast["pokehouse1"] = []

    pokehouse = PokeHouse1(525,980)
    cast["pokehouse1"].append(pokehouse)
    pokehouse = PokeHouse1(660,980)
    cast["pokehouse1"].append(pokehouse)

    bikeshop = BikeShop()
    cast["bikeshop"] = bikeshop

    poketower = PokeTower()
    cast["poketower"] = poketower

    pokegym = PokeGym()
    cast["pokegym"] = pokegym

    deptstore = DeptStore()
    cast["deptstore"] = deptstore

    fountain = Fountain(400,150)
    cast["fountains"].append(fountain)

    fountain = Fountain(430,1180)
    cast["fountains"].append(fountain)
    
    ball = PokeBall(400,200) #Behind the fountain
    cast["pokeballs"].append(ball)
    ball = PokeBall(730,85) #Bottom Right behind small rock
    cast["pokeballs"].append(ball)
    ball = PokeBall(500,420) #behind pokemart
    cast["pokeballs"].append(ball)
    ball = PokeBall(340, 621) #Behind the house
    cast["pokeballs"].append(ball)
    ball = PokeBall(95,825) #Behind Far left tree area 2
    cast["pokeballs"].append(ball)
    ball = PokeBall(700,825) #Behind Far right tree area 2
    cast["pokeballs"].append(ball)
    ball = PokeBall(725,1050) #Behind hotels area 2
    cast["pokeballs"].append(ball)
    ball = PokeBall(430,1240) #Behind fountain area 2
    cast["pokeballs"].append(ball)
    ball = PokeBall(95,1500) #Behind skyscraper area 2
    cast["pokeballs"].append(ball)
    ball = PokeBall(535,1820) #In front of mall area 2
    cast["pokeballs"].append(ball)
    ball = PokeBall(730,650) #Top Right rocks
    cast["pokeballs"].append(ball)
    ball = PokeBall(220, 410) #Behind Pokemart
    cast["pokeballs"].append(ball)

    # random.shuffle(cast["pokeballs"]) #Breaks game, too long to find all
    # ball = PokeBall(150,100)
    # cast["pokeballs"].append(ball)

    littlerock = BreakRock(655,85)
    cast["breakrock"].append(littlerock)

    littlerock = BreakRock(315, 800)
    cast["breakrock"].append(littlerock)
    littlerock = BreakRock(353, 800)
    cast["breakrock"].append(littlerock)
    littlerock = BreakRock(390, 800)
    cast["breakrock"].append(littlerock)
    
    tree = TreeHoriz(5,780)
    cast["trees"].append(tree)

    tree = TreeHoriz(183,2290)
    cast["trees"].append(tree)
    tree = TreeHoriz(767,2290)
    cast["trees"].append(tree)
    tree = TreeHoriz(183,2213)
    cast["trees"].append(tree)
    tree = TreeHoriz(767,2213)
    cast["trees"].append(tree)


    

    lefttreeside = TreeSides(4,910)
    cast["treesides"].append(lefttreeside)
    lefttreeside = TreeSides(49,910)
    cast["treesides"].append(lefttreeside)
    
    lefttreeside = TreeSides(4,400)
    cast["treesides"].append(lefttreeside)
    lefttreeside = TreeSides(49,400)
    cast["treesides"].append(lefttreeside)

    lefttreeside = TreeSides(4,1420)
    cast["treesides"].append(lefttreeside)
    lefttreeside = TreeSides(49,1420)
    cast["treesides"].append(lefttreeside)

    lefttreeside = TreeSides(4,1930)
    cast["treesides"].append(lefttreeside)
    lefttreeside = TreeSides(49,1930)
    cast["treesides"].append(lefttreeside)

    lefttreeside = TreeSides(814,1500)
    cast["treesides"].append(lefttreeside)
    lefttreeside = TreeSides(769,1500)
    cast["treesides"].append(lefttreeside)

    lefttreeside = TreeSides(814,80)
    cast["treesides"].append(lefttreeside)
    lefttreeside = TreeSides(769,80)
    cast["treesides"].append(lefttreeside)

    lefttreeside = TreeSides(814,1755)
    cast["treesides"].append(lefttreeside)
    lefttreeside = TreeSides(769,1755)
    cast["treesides"].append(lefttreeside)

    tree = TreeHoriz(700,780)
    cast["trees"].append(tree)

    for x in range(4,850,45):
        tree = Tree(x,40)
        cast["trees"].append(tree)

    for x in range(4,850,45):
        tree = Tree(x,5)
        cast["trees"].append(tree)

    for x in range(800,650,-69):
        rock = BigRock(x,700)
        cast["bigrocks"].append(rock)
    rock = BigRock(710,140)
    cast["bigrocks"].append(rock)
    rock = BigRock(770,863)
    cast["bigrocks"].append(rock)

    # for x in range(800,650,-69):
    #     rock = BigRock(x,860)
    #     cast["bigrocks"].append(rock)
    # rock = BigRock(710,140)
    # cast["bigrocks"].append(rock)
    
    
    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    handle_collections_action = HandleCollectionsAction()
    handle_breaks_action = HandleBreaksAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action,handle_collections_action,handle_breaks_action]
    script["output"] = [draw_actors_action]
    
    # start the game
    director = Director(cast, script, input_service)
    director.setup()


    starter_music = arcade.load_sound(constants.STARTER_MUSIC)
    arcade.play_sound(starter_music,looping=True, volume=0.05)
    arcade.run()

    

if __name__ == "__main__":
    main()