'''
Created on Jan 18, 2014

@author: anthony.lozano
'''
from world import World
if __name__ == '__main__':
    world = World(5,5,1, see_port="COM8")
    for i in range(20):
        world.communicate()