'''
Created on Jan 18, 2014

@author: anthony.lozano
'''
from world import World
if __name__ == '__main__':
    world = World(16,16,1, see_port="COM8")
    #world.carve_path()
    print world
    for i in range(20):
        world.communicate()
        input = raw_input()
        if input == "w":
            world.move(True)
        elif input == "a":
            world.turn(False)
        elif input == "d'":
            world.turn(True)
        elif input == "s":
            world.move(False)