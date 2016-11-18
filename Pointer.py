
import math
from visual import *

class Pointer:
    """ This class represents a three-eyed alien object...
    """

    # The constructor, named __init__ (as always in Python)
    def __init__(self, init_framepos):
        """ The constructor creates a frame (container)
            at initial location init_framepos
        """
        # a frame is VPython's collection of shapes
        # within a single coordinate system
        self.f = frame(pos=init_framepos)

        self.middlepos = vector(0,0,0)

        # all of these parts are within the frame self.f
        self.Top = box(pos=self.middlepos + vector(2.5,0,0),
                           color=color.magenta, length = .4,
                           width = 5.4, height = .4,
                           frame=self.f)

        self.Bottom = box(pos=self.middlepos + vector(-2.5,0,0),
                           color=color.magenta, length = .4,
                           width = 5.4, height = .4,
                           frame=self.f)

        self.Right = box(pos=self.middlepos + vector(0,0,2.5),
                           color=color.magenta, length = 5.4,
                           width = .4, height = .4,
                           frame=self.f)

        self.Left = box(pos=self.middlepos + vector(0,0,-2.5),
                           color=color.magenta, length = 5.4,
                           width = .4, height = .4,
                           frame=self.f)

        
        
        



