#
# cube
#

import math
from visual import *

class Cubes:
    """ This class represents a three-eyed alien object...
    """

    def __repr__(self):
        """ The printable representation of an Alien """
        s = ''
        s += "This alien is at "
        s += str( self.f.pos )
        s += " with vel = " + str( self.vel )
        return s

    # The constructor, named __init__ (as always in Python)
    def __init__(self, init_framepos):
        """ The constructor creates a frame (container)
            at initial location init_framepos
        """
        # a frame is VPython's collection of shapes
        # within a single coordinate system
        self.f = frame(pos=init_framepos)

        # the alien's velocity
        self.vel = vector(0,0,0)

        # all of these parts are within the frame self.f
        self.cube = box(pos=vector(0,0,0),
                           color=color.black, length = 5,
                           width = 5, height = 5,
                           frame=self.f)

        self.white = box(pos=self.cube.pos+vector(0,2.5,0), color = color.white,
                         length = 4.8, width = 4.8, height = 0.2,
                         frame=self.f)

        self.yellow = box(pos=self.cube.pos+vector(0,-2.5,0), color = color.yellow,
                         length = 4.8, width = 4.8, height = 0.2,
                         frame=self.f)

        self.red = box(pos=self.cube.pos+vector(2.5,0,0), color = color.red,
                         length = 0.2, width = 4.8, height = 4.8,
                         frame=self.f)

        self.orange = box(pos=self.cube.pos+vector(-2.5,0,0), color = color.orange,
                         length = 0.2, width = 4.8, height = 4.8,
                         frame=self.f)

        self.blue = box(pos=self.cube.pos+vector(0,0,-2.5), color = color.blue,
                         length = 4.8, width = 0.2, height = 4.8,
                         frame=self.f)

        self.green = box(pos=self.cube.pos+vector(0,0,2.5), color = color.green,
                         length = 4.8, width = 0.2, height = 4.8,
                         frame=self.f)
        
        


    def check_for_collision( self, collider, r ):
        """ checks for a collision with the collider
            at a radius of r
        """
        # mag is the magnitude of a vector, similar to abs for numbers
        if mag( self.f.pos - collider.pos ) < r:
            return True  # collided (within r)
        else:
            return False



