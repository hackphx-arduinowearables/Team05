'''
Created on Jan 18, 2014

@author: anthony.lozano
'''
import unittest
from world import World

class Test(unittest.TestCase):


    def testWorld(self):
        new_world = World(3,3,3)
        print new_world
        
    def testCarve(self):
        new_world = World(5,4,3)
        new_world.carve_path()
        print new_world


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testWorld']
    unittest.main()