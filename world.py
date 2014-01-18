'''
Created on Jan 18, 2014

@author: anthony.lozano
'''
import random
from collections import deque
import math
from serial import Serial
from bitstring import BitArray
from copy import copy

blocks = {"empty" : 1,
          "wall"  : 2,
          "hazard": 3,
          }
headings = ["n", "s", "e", "w", "ne", "nw", "sw", "se"]

class World(object):
    '''
    classdocs
    '''


    def __init__(self, width= 10, length= 10, hieght=2, hear_port="COM5", see_port="COM5", feel_port="COM5"):
        '''
        Constructor
        '''
        self.width = width
        self.length = length
        self.hieght = hieght
        
        self.world_grid = [[[blocks['empty'] * hieght] * length] * width]
        self.w, self.l, self.h = (0,0,0)
        self.goal = (width, length, hieght)
        self.heading = deque( [
                               (0, 1)  ,
                               (-1, -1),
                               (-1, 0) ,
                               (-1, 1) ,
                               (0, -1) ,
                               (-1, -1),
                               (1, 0)  ,
                               (1, 1)  ,
                               ]
                        )
        #self.hear_conn = Serial(hear_port, 115200)
        #self.see_conn =  Serial(see_port, 115200)
        #self.feel_conn = Serial(feel_port, 115200)

    def get_heading(self):
        '''
        retuns w, l, where w, l is the offsets you would add if you moved forward at this heading
        '''
        return self.heading[0]

    def get_pos(self, off_w=0, off_l=0, off_h=0):
        '''
        Gets the current avatar position or the current position plus an offset
        :param off_w: w offset
        :param off_l: l offset
        :param off_z: z offset
        :return: current pos val, plus offset
        '''
        try:
            return self.world_grid[self.w + off_w][self.l + off_l][self.h + off_h]
        except IndexError:
            return blocks['wall']
    
    def carve_path(self):
        '''
        creates a random world of walls and cuts a path to the goal
        '''
        final = self.length # once we reach the last length, we set the goal and terminate
        w, l, h = 0, 0, 0 # start at 0,0,0
        last_move_name, last_move_tuple = "forward", (0,1,0) # we don't want to repeat the last movement
        moves = {"back": (0,-1,0), "left": (-1, 0, 0), "right": (1, 0, 0), "up": (0,0,1), "down": (0,0,-1)} #possible moves
        self.world_grid[w][l][h] = blocks["empty"] #set the current block empty
        while l != final:
            move, (m_w, m_l, m_h) = random.choice(list(moves.iteritems())) #get a move
            w += m_w  #apply move
            l += m_l
            h += m_h
            self.world_grid[w][l][h] = blocks["empty"] #set that cell empty
            moves[last_move_name] = last_move_tuple # add back in the last move to movelist
            last_move_name, last_move_tuple = move, (m_w, m_l, m_h) #copy the current move to last move
            moves.pop(last_move_name) #remove the current
        self.goal = (w,l,h) #after terminating, set this as the goal
            
    def listen(self):
        '''
        searchs up and down for the distance to walls and returns the distance. Can also return block types in the future
        '''
        up_distance, above = self.search(0, 0, 1)
        down_distance, below = self.search(0, 0, -1)
        return above, up_distance, below, down_distance
    
    def search(self, w, l, h):
        '''
        :param w: steps w per tick
        :param l: steps l per tick
        :param h: steps h per tick
        given a heading, continues in that direction until it finds a non-empty voxel
        @return distance, block_type
        '''
        c_w, c_l, c_h = w,l,h
        distance = 0
        while self.get_pos(c_w, c_l, c_h) == blocks['empty']:
            c_w += w
            c_l += l
            c_h += h
        distance += int(math.floor(math.sqrt(c_w**2+c_l**2+c_h**2)))
        return distance, self.get_pos(c_w, c_l, c_h)

    def look(self):
        '''
        returns a list from left to right what each LED should see. 5 directions, 5 objects, 5 distances
        '''
        heading_queue = copy(self.heading)
        heading_queue.rotate(-2)
        headings = list(heading_queue)[:5] #gives a list of 5 headings from leftmost to rightmost
        LED_list = []
        for w, l in headings:
            LED_list.append(self.search(w, l, 0))
        return LED_list

    def move(self, is_forward):
        '''
        moves the avatar position in the direction of heading if is_forward is true, opposite direction otherwise
        :param is_forward: boolean flag for forward motion. Reverse motion if false
        '''
        wh, lh= self.get_heading()
        self.w += wh
        self.l += lh
        if self.get_pos() == blocks['wall']:
            self.w -= wh
            self.l -= lh
            
    
    def up_down(self, up):
        '''
        move the avatar on the Z axis up or down
        :param up: boolean flag moves up if true, false otherwise
        '''
        if up == 'u':
            up = 1
        elif up == 'n':
            up = 0
        elif up == 'd':
            up = -1
        else:
            raise ValueError("The heck you doing Servo?? u d or n ONLY")
        self.h += up
        if self.get_pos() == blocks['wall']:
            self.h -= up
    
    def turn(self, is_right):
        '''
        turns the avatars heading by rotating the heading circular list
        :param is_right: true if we are turning right, false otherwise
        '''
        if is_right:
            self.heading.rotate(1)
        else:
            self.heading.rotate(-1)
    
    def find_goal(self):
        '''
        Get the heading for the goal
        
        '''
        w, l, h = self.get_pos()
        gw, gl, gh = self.goal 
        try:
            angle_deg = angle((w,l),(gw,gl))
        except ZeroDivisionError:
            if w > gw and l > gl:
                return 2
            elif w < gw and l < gl:
                return 5
        if -105 <= angle_deg <= -75:
            return 0
        elif -75 < angle_deg < 15:
            return 1
        elif -15 <= angle_deg <= 15:
            return 2
        elif 15 < angle_deg < 75:
            return 3
        elif 75 <= angle_deg <= 105:
            return 4
        else:
            return 5
        
    def communicate(self):
#        turn = self.hear_conn.read()
        #self.up_down(self.hear_conn.read())
        #above, up_distance, below, down_distance = self.listen()
        LEDs = self.look()
        byte_seq = (BitArray("0b11") 
                + BitArray(uint=LEDs[0][0], length=2)
                + BitArray(uint=LEDs[0][1], length=4)
                + BitArray(uint=LEDs[1][0], length=4)
                + BitArray(uint=LEDs[1][1], length=4)
                + BitArray(uint=LEDs[2][0], length=4)
                + BitArray(uint=LEDs[2][1], length=4)
                + BitArray(uint=LEDs[3][0], length=4)
                + BitArray(uint=LEDs[3][1], length=4)
                + BitArray(uint=LEDs[4][0], length=4)
                + BitArray(uint=LEDs[4][1], length=4)
                )
        self.hear_conn.write(byte_seq.bytes)
        print self.see_conn.read()

def angle(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    inner_product = x1*x2 + y1*y2
    len1 = math.hypot(x1, y1)
    len2 = math.hypot(x2, y2)
    return math.acos(inner_product/(len1*len2))
   