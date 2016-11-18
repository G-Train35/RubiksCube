import math
from time import sleep
import random
from visual import *
from RubiksCube import *
import rubiksCubeSolver
from Pointer import *
import numpy as np
#import cv2

def Positive(Pivot,p1,p2,p3,p4,p5,p6,p7,p8,A):
    point = Pivot.cube.pos
    Pivot.f.rotate(angle=pi/40,axis=A, origin=point)
    p1.f.rotate(angle=pi/40,axis=A, origin=point)
    p2.f.rotate(angle=pi/40,axis=A, origin=point)
    p3.f.rotate(angle=pi/40,axis=A, origin=point)
    p4.f.rotate(angle=pi/40,axis=A, origin=point)
    p5.f.rotate(angle=pi/40,axis=A, origin=point)
    p6.f.rotate(angle=pi/40,axis=A, origin=point)
    p7.f.rotate(angle=pi/40,axis=A, origin=point)
    p8.f.rotate(angle=pi/40,axis=A, origin=point)

def Negative(Pivot,p1,p2,p3,p4,p5,p6,p7,p8,A):
    point = Pivot.cube.pos
    Pivot.f.rotate(angle=-pi/40,axis=A, origin=point)
    p1.f.rotate(angle=-pi/40,axis=A, origin=point)
    p2.f.rotate(angle=-pi/40,axis=A, origin=point)
    p3.f.rotate(angle=-pi/40,axis=A, origin=point)
    p4.f.rotate(angle=-pi/40,axis=A, origin=point)
    p5.f.rotate(angle=-pi/40,axis=A, origin=point)
    p6.f.rotate(angle=-pi/40,axis=A, origin=point)
    p7.f.rotate(angle=-pi/40,axis=A, origin=point)
    p8.f.rotate(angle=-pi/40,axis=A, origin=point)

def Color(S):
    if S == 'W':
        return color.white
    elif S == 'Y':
        return color.yellow
    elif S == 'G':
        return color.green
    elif S == 'B':
        return color.blue
    elif S == 'R':
        return color.red
    elif S == 'O':
        return color.orange
    else:
        return color.black

def Opposites(S):
    if S == 'Y':
        return color.white
    elif S == 'W':
        return color.yellow
    elif S == 'B':
        return color.green
    elif S == 'G':
        return color.blue
    elif S == 'O':
        return color.red
    else:
        return color.orange

def ResetPiece(Piece):
    Piece.white.color = color.white
    Piece.yellow.color = color.yellow
    Piece.red.color = color.red
    Piece.orange.color = color.orange
    Piece.blue.color = color.blue
    Piece.green.color = color.green

def CreateBlack(Piece):
    Piece.white.color = (.2,.2,.2)
    Piece.yellow.color = (.2,.2,.2)
    Piece.red.color = (.2,.2,.2)
    Piece.orange.color = (.2,.2,.2)
    Piece.blue.color = (.2,.2,.2)
    Piece.green.color = (.2,.2,.2)
            
def VisualImport(Piece,CPiece,Top,North,East):
    adj = 0
    if Top != 'X':
        if Top:
            Piece.white.color = Color(CPiece[0])
        else:
            Piece.yellow.color = Color(CPiece[0])
    else:
        adj = 1
    if North != 'X':
        if North:
            Piece.red.color = Color(CPiece[1-adj])
        else:
            Piece.orange.color = Color(CPiece[1-adj])
    else:
        adj = 1
    if East != 'X':
        if East:
            Piece.green.color = Color(CPiece[2-adj])
        else:
            Piece.blue.color = Color(CPiece[2-adj])


def Import():
    C = rubiksCubeSolver.cube()

    Test = CropCube("WhiteFullTest.jpg")
    White = FindColors(Test)

    Test = CropCube("YellowFullTest.jpg")
    Yellow = FindColors(Test)

    Test = CropCube("RedFullTest.jpg")
    Red = FindColors(Test)

    Test = CropCube("OrangeFullTest.jpg")
    Orange = FindColors(Test)

    Test = CropCube("GreenFullTest.jpg")
    Green = FindColors(Test)

    Test = CropCube("BlueFullTest.jpg")
    Blue = FindColors(Test)

    WOG = White[0]
    WG = White[1]
    WRG = White[2]
    WR = White[3]
    WRB = White[4]
    WB = White[5]
    WOB = White[6]
    WO = White[7]

    YOB = Yellow[0]
    YB = Yellow[1]
    YRB = Yellow[2]
    YR = Yellow[3]
    YRG = Yellow[4]
    YG = Yellow[5]
    YOG = Yellow[6]
    YO = Yellow[7]

    WRG += Red[0]
    RG = Red[1]
    YRG += Red[2]
    YR += Red[3]
    YRB += Red[4]
    RB = Red[5]
    WRB += Red[6]
    WR += Red[7]

    WOB += Orange[0]
    OB = Orange[1]
    YOB += Orange[2]
    YO += Orange[3]
    YOG += Orange[4]
    OG = Orange[5]
    WOG += Orange[6]
    WO += Orange[7]

    WOG += Green[0]
    OG += Green[1]
    YOG += Green[2]
    YG += Green[3]
    YRG += Green[4]
    RG += Green[5]
    WRG += Green[6]
    WG += Green[7]

    WRB += Blue[0]
    RB += Blue[1]
    YRB += Blue[2]
    YB += Blue[3]
    YOB += Blue[4]
    OB += Blue[5]
    WOB += Blue[6]
    WB += Blue[7]



    C.TopNW = (WRB[0],WRB[1],WRB[2])
    
    C.TopN = (WR[0],WR[1])
    
    C.TopNE = (WRG[0],WRG[1],WRG[2])

    C.TopW = (WB[0],WB[1])

    C.TopE = (WG[0],WG[1])

    C.TopSE = (WOG[0],WOG[1],WOG[2])
    
    C.TopS = (WO[0],WO[1])
    
    C.TopSW = (WOB[0],WOB[1],WOB[2])

    C.MiddleNW = (RB[0],RB[1])
    
    C.MiddleNE = (RG[0],RG[1])

    C.MiddleSW = (OB[0],OB[1])
    
    C.MiddleSE = (OG[0],OG[1])
    
    C.BottomNW = (YRB[0],YRB[1],YRB[2])
    
    C.BottomN = (YR[0],YR[1])
    
    C.BottomNE = (YRG[0],YRG[1],YRG[2])

    C.BottomW = (YB[0],YB[1])

    C.BottomE = (YG[0],YG[1])
    
    C.BottomSW = (YOB[0],YOB[1],YOB[2])
    
    C.BottomS = (YO[0],YO[1])
    
    C.BottomSE = (YOG[0],YOG[1],YOG[2])

    return C
    
"""
def CropCube(name):
    img = cv2.imread(name,3)
    img = cv2.resize(img, (img.shape[1]/2, img.shape[0]/2))

    tempImg = np.zeros((16,4,3), np.uint8)
    tempImg[:,0:2] = (220,220,220)

    OutPut = cv2.matchTemplate(img, tempImg, 1)
    OutPut = cv2.resize(OutPut, (OutPut.shape[1]/10, OutPut.shape[0]/10))
    newimg = cv2.resize(img, (img.shape[1]/10, img.shape[0]/10))

    rows = OutPut.shape[0]
    cols = OutPut.shape[1]

    Leftmed = []
    for i in range(rows):
        found = False
        j = 0
        while found != True:
            if OutPut[i][j] > 0.95:
                newimg[i][j] = [255,255,0]
                Leftmed += [j]
                found = True
            j+=1
            if j > cols-1:
                found = True

    lMed = int(median(Leftmed))

    tempImg = np.zeros((16,4,3), np.uint8)
    tempImg[:,2:4] = (220,220,220)

    OutPut2 = cv2.matchTemplate(img, tempImg, 1)
    OutPut2 = cv2.resize(OutPut2, (OutPut2.shape[1]/10, OutPut2.shape[0]/10))

    rightmed = []
    for i in range(rows):
        found = False
        j = cols-1
        while found != True:
            if OutPut2[i][j] > 0.95:
                newimg[i][j] = [255,255,0]
                rightmed += [j]
                found = True
            j-=1
            if j < 0:
                found = True

    rMed = int(median(rightmed))




    tempImg = np.zeros((4,16,3), np.uint8)
    tempImg[2:4,:] = (220,220,220)

    OutPut = cv2.matchTemplate(img, tempImg, 1)
    OutPut = cv2.resize(OutPut, (OutPut.shape[1]/10, OutPut.shape[0]/10))

    rows = OutPut.shape[0]
    cols = OutPut.shape[1]

    bottomMed = []
    for j in range(cols):
        found = False
        i = rows-1
        while found != True:
            if OutPut[i][j] > 0.95:
                newimg[i][j] = [255,255,0]
                bottomMed += [i]
                found = True
            i-=1
            if i < 0:
                found = True

    bMed = int(median(bottomMed))

    tempImg = np.zeros((4,16,3), np.uint8)
    tempImg[0:2,:] = (220,220,220)

    OutPut2 = cv2.matchTemplate(img, tempImg, 1)
    OutPut2 = cv2.resize(OutPut2, (OutPut2.shape[1]/10, OutPut2.shape[0]/10))

    topmed = []
    for j in range(cols):
        found = False
        i = 0
        while found != True:
            if OutPut2[i][j] > 0.95:
                newimg[i][j] = [255,255,0]
                topmed += [i]
                found = True
            i+=1
            if i > rows-1:
                found = True

    tMed = int(median(topmed))

    
    cv2.imshow('the',newimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

    newimg = newimg[tMed:bMed,lMed:rMed]

    return newimg
"""

def FindColors(img):

    rows = img.shape[0]
    cols = img.shape[1]

    color1r = []
    color1g = []
    color1b = []
    for i in range(rows/9,2*rows/9):
        for j in range(cols/9,2*cols/9):
            if int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2]) < 150:
                continue
            color1r += [int(img[i][j][0])]
            color1g += [int(img[i][j][1])]
            color1b += [int(img[i][j][2])]

    color2r = []
    color2g = []
    color2b = []
    for i in range(4*rows/9,5*rows/9):
        for j in range(cols/9,2*cols/9):
            if int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2]) < 150:
                continue
            color2r += [int(img[i][j][0])]
            color2g += [int(img[i][j][1])]
            color2b += [int(img[i][j][2])]

    color3r = []
    color3g = []
    color3b = []
    for i in range(7*rows/9,8*rows/9):
        for j in range(cols/9,2*cols/9):
            if int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2]) < 150:
                continue
            color3r += [int(img[i][j][0])]
            color3g += [int(img[i][j][1])]
            color3b += [int(img[i][j][2])]

    color4r = []
    color4g = []
    color4b = []
    for i in range(7*rows/9,8*rows/9):
        for j in range(4*cols/9,5*cols/9):
            if int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2]) < 150:
                continue
            color4r += [int(img[i][j][0])]
            color4g += [int(img[i][j][1])]
            color4b += [int(img[i][j][2])]

    color5r = []
    color5g = []
    color5b = []
    for i in range(7*rows/9,8*rows/9):
        for j in range(7*cols/9,8*cols/9):
            if int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2]) < 150:
                continue
            color5r += [int(img[i][j][0])]
            color5g += [int(img[i][j][1])]
            color5b += [int(img[i][j][2])]

    color6r = []
    color6g = []
    color6b = []
    for i in range(4*rows/9,5*rows/9):
        for j in range(7*cols/9,8*cols/9):
            if int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2]) < 150:
                continue
            color6r += [int(img[i][j][0])]
            color6g += [int(img[i][j][1])]
            color6b += [int(img[i][j][2])]

    color7r = []
    color7g = []
    color7b = []
    for i in range(rows/9,2*rows/9):
        for j in range(7*cols/9,8*cols/9):
            if int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2]) < 150:
                continue
            color7r += [int(img[i][j][0])]
            color7g += [int(img[i][j][1])]
            color7b += [int(img[i][j][2])]

    color8r = []
    color8g = []
    color8b = []
    for i in range(rows/9,2*rows/9):
        for j in range(4*cols/9,5*cols/9):
            if int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2]) < 150:
                continue
            color8r += [int(img[i][j][0])]
            color8g += [int(img[i][j][1])]
            color8b += [int(img[i][j][2])]

    color1 = [median(color1r),median(color1g),median(color1b)]
    color2 = [median(color2r),median(color2g),median(color2b)]
    color3 = [median(color3r),median(color3g),median(color3b)]
    color4 = [median(color4r),median(color4g),median(color4b)]
    color5 = [median(color5r),median(color5g),median(color5b)]
    color6 = [median(color6r),median(color6g),median(color6b)]
    color7 = [median(color7r),median(color7g),median(color7b)]
    color8 = [median(color8r),median(color8g),median(color8b)]

    colorarray = []

    colorarray += [DetermineColor(color1)]
    colorarray += [DetermineColor(color2)]
    colorarray += [DetermineColor(color3)]
    colorarray += [DetermineColor(color4)]
    colorarray += [DetermineColor(color5)]
    colorarray += [DetermineColor(color6)]
    colorarray += [DetermineColor(color7)]
    colorarray += [DetermineColor(color8)]

    return colorarray

def DetermineColor(color):
    if color[0] < 100 and color[1] > 130 and color[2] > 150:
        print (color[0],color[1],color[2]) 
        print 'Y'
        return 'Y'
    elif color[0] > 130 and color[1] > 130 and color[2] > 130:
        print (color[0],color[1],color[2]) 
        print 'W'
        return 'W'
    elif color[0] < 120 and color[1] > 80 and color[1] < 180 and color[2] < 100:
        print (color[0],color[1],color[2]) 
        print 'G'
        return 'G'
    elif color[0] > 50 and color[0] < 180 and color[1] < 80 and color[2] < 80:
        print (color[0],color[1],color[2]) 
        print 'B'
        return 'B'
    elif color[0] < 80 and color[1] < 80 and color[2] > 100 and color[2] < 190:
        print (color[0],color[1],color[2]) 
        print 'R'
        return 'R'
    elif color[0] < 80 and color[1] < 150 and color[1] > 50 and color[2] > 190:
        print (color[0],color[1],color[2]) 
        print 'O'
        return 'O'
    else:
        print (color[0],color[1],color[2])
        return 'Error'
    

    

def main():
    """ The main game function.
    """
    C = rubiksCubeSolver.cube()

    Teach = False

    Interior = box(pos = (0,0,0), color = color.black, length = 5,
                width = 5, height = 5)
    WRB = Cubes( (5,5,-5) )
    
    WR = Cubes( (5,5,0) )
    
    WRG = Cubes( (5,5,5) )
    
    YRB = Cubes( (5,-5,-5) )
    
    YR = Cubes( (5,-5,0) )
    
    YRG = Cubes( (5,-5,5) )
    
    RB = Cubes( (5,0,-5) )
    
    R = Cubes( (5,0,0) )
    
    RG = Cubes( (5,0,5) )
    
    WOB = Cubes( (-5,5,-5) )
    
    WO = Cubes( (-5,5,0) )
    
    WOG = Cubes( (-5,5,5) )
    
    YOB = Cubes( (-5,-5,-5) )
    
    YO = Cubes( (-5,-5,0) )
    
    YOG = Cubes( (-5,-5,5) )
    
    OB = Cubes( (-5,0,-5) )
    
    O = Cubes( (-5,0,0) )
    
    OG = Cubes( (-5,0,5) )

    WG = Cubes( (0,5,5) )
    
    G = Cubes( (0,0,5) )
    
    YG = Cubes( (0,-5,5) )

    WB = Cubes( (0,5,-5) )
    
    B = Cubes( (0,0,-5) )
    
    YB = Cubes( (0,-5,-5) )

    W = Cubes( (0,5,0) )

    Y = Cubes( (0,-5,0) )

    T = text(text='',pos = (0,20,0),height = 2, align='center', color=color.white,axis=(1,0,1))
    
    
    scene.range = 35
    scene.forward = vector(-.1,-.1,-.1) # look downward
    scene.autoscale = False
    
    
    close = 2.0 # click this close to tail or tip
    drag = None # remembers if we're dragging...

    
    
    RATE = 10        # maximum update rate (in hertz)
    dt = 1.0/RATE       # time per loop
    scene.autoscale = False    # helpful for viewing
    # the main simulation loop
    time = 0
    while True:
        time += 1
        rate(RATE)  # this many times per second, at most

        #Interior.rotate(angle=pi/4, axis=(0,1,0), origin=(0,0,0))
        #R.rotate(angle=pi/8,axis=(0,1,0), origin=(0,0,0))

        # handle mouse and keyboard events
        #
        if scene.mouse.clicked != 0: # is there a mouse click?
            print scene.forward
            event = scene.mouse.getclick() # remove event
            scene.mouse.events = 0   # then reset mouse events
            
        if scene.kb.keys:            # is there a keyevent?
            s = scene.kb.getkey()    # get keypress
            print "keypress is", s
            
            # move the center of the viewing window
            if s == 'I':
                Teach = True
                RATE = 3
                CreateBlack(WRB)
                
                CreateBlack(WR)
                
                CreateBlack(WRG)
                
                CreateBlack(YRB)
                
                CreateBlack(YR)
                
                CreateBlack(YRG)
                
                CreateBlack(RB)
                
                CreateBlack(RG)
                
                CreateBlack(WOB)
                
                CreateBlack(WO)
                
                CreateBlack(WOG)
                
                CreateBlack(YOB)
                
                CreateBlack(YO)
                
                CreateBlack(YOG)
                
                CreateBlack(OB)
                
                CreateBlack(OG)

                CreateBlack(WG)
                
                CreateBlack(YG)

                CreateBlack(WB)
                
                CreateBlack(YB)

                
                scene.forward = (-.33,-.94,0)
                PointerW = Pointer( (5.2,7.7,5.2) )
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Tne = key
                WRG.white.color = Color(Tne)

                PointerW.f.pos = (0,7.7,5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Te = key
                WG.white.color = Color(Te)

                PointerW.f.pos = (-5.2,7.7,5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Tse = key
                WOG.white.color = Color(Tse)

                PointerW.f.pos = (-5.2,7.7,0)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Ts = key
                WO.white.color = Color(Ts)

                PointerW.f.pos = (-5.2,7.7,-5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Tsw = key
                WOB.white.color = Color(Tsw)

                PointerW.f.pos = (0,7.7,-5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Tw = key
                WB.white.color = Color(Tw)

                PointerW.f.pos = (5.2,7.7,-5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Tnw = key
                WRB.white.color = Color(Tnw)

                PointerW.f.pos = (5.2,7.7,0)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Tn = key
                WR.white.color = Color(Tn)

                for i in range(1,11):
                    scene.forward = (-.33 - .06*i,-.94 + .06*i,0)
                    rate(20)

                PointerW.f.rotate(angle=pi/2,axis=(0,0,1), origin=PointerW.f.pos)
                PointerW.f.pos = (7.7,5.2,5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                tNe = key
                WRG.red.color = Color(tNe)

                PointerW.f.pos = (7.7,0,5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                mNe = key
                RG.red.color = Color(mNe)

                PointerW.f.pos = (7.7,-5.2,5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                bNe = key
                YRG.red.color = Color(bNe)

                
                PointerW.f.pos = (7.7,-5.2,0)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                bN = key
                YR.red.color = Color(bN)

                PointerW.f.pos = (7.7,-5.2,-5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                bNw = key
                YRB.red.color = Color(bNw)

                PointerW.f.pos = (7.7,0,-5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                mNw = key
                RB.red.color = Color(mNw)

                PointerW.f.pos = (7.7,5.2,-5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                tNw = key
                WRB.red.color = Color(tNw)

                PointerW.f.pos = (7.7,5.2,0)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                tN = key
                WR.red.color = Color(tN)


                for i in range(1,11):
                    scene.forward = (-.93 + .095*i,-.34,0.095*i)
                    rate(20)

                PointerW.f.rotate(angle=pi/2,axis=(0,1,0), origin=PointerW.f.pos)
                PointerW.f.pos = (5.2,5.2,-7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                tnW = key
                WRB.blue.color = Color(tnW)

                PointerW.f.pos = (5.2,0,-7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                mnW = key
                RB.blue.color = Color(mnW)

                PointerW.f.pos = (5.2,-5.2,-7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                bnW = key
                YRB.blue.color = Color(bnW)

                PointerW.f.pos = (0,-5.2,-7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                bW = key
                YB.blue.color = Color(bW)

                PointerW.f.pos = (-5.2,-5.2,-7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                bsW = key
                YOB.blue.color = Color(bsW)

                PointerW.f.pos = (-5.2,0,-7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                msW = key
                OB.blue.color = Color(msW)

                PointerW.f.pos = (-5.2,5.2,-7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                tsW = key
                WOB.blue.color = Color(tsW)

                PointerW.f.pos = (0,5.2,-7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                tW = key
                WB.blue.color = Color(tW)

                for i in range(1,11):
                    scene.forward = (.095*i,-.34,.95 - .095*i)
                    rate(20)

                PointerW.f.rotate(angle=pi/2,axis=(0,1,0), origin=PointerW.f.pos)
                PointerW.f.pos = (-7.7,5.2,-5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                tSw = key
                WOB.orange.color = Color(tSw)

                PointerW.f.pos = (-7.7,0,-5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                mSw = key
                OB.orange.color = Color(mSw)

                PointerW.f.pos = (-7.7,-5.2,-5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                bSw = key
                YOB.orange.color = Color(bSw)
                
                PointerW.f.pos = (-7.7,-5.2,0)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                bS = key
                YO.orange.color = Color(bS)

                PointerW.f.pos = (-7.7,-5.2,5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                bSe = key
                YOG.orange.color = Color(bSe)

                PointerW.f.pos = (-7.7,0,5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                mSe = key
                OG.orange.color = Color(mSe)

                PointerW.f.pos = (-7.7,5.2,5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                tSe = key
                WOG.orange.color = Color(tSe)

                PointerW.f.pos = (-7.7,5.2,0)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                tS = key
                WO.orange.color = Color(tS)

                for i in range(1,11):
                    scene.forward = (.95 - .095*i,-.34,-.095*i)
                    rate(20)

                PointerW.f.rotate(angle=pi/2,axis=(0,1,0), origin=PointerW.f.pos)
                PointerW.f.pos = (-5.2,5.2,7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                tsE = key
                WOG.green.color = Color(tsE)

                PointerW.f.pos = (-5.2,0,7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                msE = key
                OG.green.color = Color(msE)

                PointerW.f.pos = (-5.2,-5.2,7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                bsE = key
                YOG.green.color = Color(bsE)

                PointerW.f.pos = (0,-5.2,7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                bE = key
                YG.green.color = Color(bE)

                PointerW.f.pos = (5.2,-5.2,7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                bnE = key
                YRG.green.color = Color(bnE)

                PointerW.f.pos = (5.2,0,7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                mnE = key
                RG.green.color = Color(mnE)

                PointerW.f.pos = (5.2,5.2,7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                tnE = key
                WRG.green.color = Color(tnE)

                PointerW.f.pos = (0,5.2,7.7)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                tE = key
                WG.green.color = Color(tE)

                
                for i in range(1,11):
                    scene.forward = (0,.134*i -.34,-.95 +.05*i)
                    rate(20)

                PointerW.f.rotate(angle=pi/2,axis=(1,0,0), origin=PointerW.f.pos)
                PointerW.f.pos = (-5.2,-7.7,5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Bse = key
                YOG.yellow.color = Color(Bse)

                PointerW.f.pos = (-5.2,-7.7,0)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Bs = key
                YO.yellow.color = Color(Bs)

                PointerW.f.pos = (-5.2,-7.7,-5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Bsw = key
                YOB.yellow.color = Color(Bsw)

                PointerW.f.pos = (0,-7.7,-5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Bw = key
                YB.yellow.color = Color(Bw)

                PointerW.f.pos = (5.2,-7.7,-5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Bnw = key
                YRB.yellow.color = Color(Bnw)

                PointerW.f.pos = (5.2,-7.7,0)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Bn = key
                YR.yellow.color = Color(Bn)

                PointerW.f.pos = (5.2,-7.7,5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Bne = key
                YRG.yellow.color = Color(Bne)

                PointerW.f.pos = (0,-7.7,5.2)
                rate(RATE)
                scene.waitfor('keydown')
                key = scene.kb.getkey()
                Be = key
                YG.yellow.color = Color(Be)

                C.TopN = (Tn,tN) 
                C.TopE = (Te,tE)
                C.TopS = (Ts,tS)
                C.TopW = (Tw,tW)

                C.BottomN = (Bn,bN)
                C.BottomE = (Be,bE)
                C.BottomS = (Bs,bS)
                C.BottomW = (Bw,bW)

                C.MiddleNE = (mNe,mnE)
                C.MiddleNW = (mNw,mnW)
                C.MiddleSE = (mSe,msE)
                C.MiddleSW = (mSw,msW)

                C.TopNE = (Tne,tNe,tnE)
                C.TopNW = (Tnw,tNw,tnW)
                C.TopSE = (Tse,tSe,tsE)
                C.TopSW = (Tsw,tSw,tsW)
                
                C.BottomNE = (Bne,bNe,bnE)
                C.BottomNW = (Bnw,bNw,bnW)
                C.BottomSE = (Bse,bSe,bsE)
                C.BottomSW = (Bsw,bSw,bsW)

                PointerW.f.pos = (0,0,0)

                scene.forward = (1,1,1)

                RATE = 20
                
            if s == 'i':
                ResetPiece(WRB)
                
                ResetPiece(WR)
                
                ResetPiece(WRG)
                
                ResetPiece(YRB)
                
                ResetPiece(YR)
                
                ResetPiece(YRG)
                
                ResetPiece(RB)
                
                ResetPiece(RG)
                
                ResetPiece(WOB)
                
                ResetPiece(WO)
                
                ResetPiece(WOG)
                
                ResetPiece(YOB)
                
                ResetPiece(YO)
                
                ResetPiece(YOG)
                
                ResetPiece(OB)
                
                ResetPiece(OG)

                ResetPiece(WG)
                
                ResetPiece(YG)

                ResetPiece(WB)
                
                ResetPiece(YB)
                
                C = Import()
                VisualImport(WR,C.TopN,True,True,'X')
                VisualImport(WG,C.TopE,True,'X',True)
                VisualImport(WO,C.TopS,True,False,'X')
                VisualImport(WB,C.TopW,True,'X',False)

                VisualImport(YR,C.BottomN,False,True,'X')
                VisualImport(YG,C.BottomE,False,'X',True)
                VisualImport(YO,C.BottomS,False,False,'X')
                VisualImport(YB,C.BottomW,False,'X',False)

                VisualImport(RB,C.MiddleNW,'X',True,False)
                VisualImport(RG,C.MiddleNE,'X',True,True)
                VisualImport(OB,C.MiddleSW,'X',False,False)
                VisualImport(OG,C.MiddleSE,'X',False,True)

                VisualImport(WRG,C.TopNE,True,True,True)
                VisualImport(WRB,C.TopNW,True,True,False)
                VisualImport(WOG,C.TopSE,True,False,True)
                VisualImport(WOB,C.TopSW,True,False,False)

                VisualImport(YRG,C.BottomNE,False,True,True)
                VisualImport(YRB,C.BottomNW,False,True,False)
                VisualImport(YOG,C.BottomSE,False,False,True)
                VisualImport(YOB,C.BottomSW,False,False,False)

                Teach = True
                
                    
            if s == 'Z':
                scene.range = int(scene.range[0]) + 5
            if s == 'z':
                if scene.range[0] < 8:
                    print 'cant get any closer'
                else:
                    scene.range = int(scene.range[0]) - 5
            """
            if s == "W":
                for i in range(20):
                    Positive(W,WRB,WR,WRG,WB,WG,WOB,WO,WOG,(0,1,0))
                    time += 1
                    rate(RATE)
                Temp = WRG
                WRG = WRB
                WRB = WOB
                WOB = WOG
                WOG = Temp
                TempE = WG
                WG = WR
                WR = WB
                WB = WO
                WO = TempE
                C.TopC()
            if s == "w":
                for i in range(20):
                    Negative(W,WRB,WR,WRG,WB,WG,WOB,WO,WOG,(0,1,0))
                    time += 1
                    rate(RATE)
                Temp = WRG
                WRG = WOG
                WOG = WOB
                WOB = WRB
                WRB = Temp
                TempE = WR
                WR = WG
                WG = WO
                WO = WB
                WB = TempE
                C.TopCC()
                    
            if s == "b":
                for i in range(20):
                    Positive(B,WRB,YB,YRB,WB,RB,WOB,OB,YOB,(0,0,1))
                    time += 1
                    rate(RATE)
                Temp = WOB
                WOB = WRB
                WRB = YRB
                YRB = YOB
                YOB = Temp
                TempE = WB
                WB = RB
                RB = YB
                YB = OB
                OB = TempE
                C.WestC()
            if s == "B":
                for i in range(20):
                    Negative(B,WRB,YB,YRB,WB,RB,WOB,OB,YOB,(0,0,1))
                    time += 1
                    rate(RATE)
                Temp = WOB
                WOB = YOB
                YOB = YRB
                YRB = WRB
                WRB = Temp
                TempE = WB
                WB = OB
                OB = YB
                YB = RB
                RB = TempE
                C.WestCC()
            if s == "G":
                for i in range(20):
                    Positive(G,WRG,YG,YRG,WG,RG,WOG,OG,YOG,(0,0,1))
                    time += 1
                    rate(RATE)
                Temp = WOG
                WOG = WRG
                WRG = YRG
                YRG = YOG
                YOG = Temp
                TempE = WG
                WG = RG
                RG = YG
                YG = OG
                OG = TempE
                C.EastCC()
            if s == "g":
                for i in range(20):
                    Negative(G,WRG,YG,YRG,WG,RG,WOG,OG,YOG,(0,0,1))
                    time += 1
                    rate(RATE)
                Temp = WOG
                WOG = YOG
                YOG = YRG
                YRG = WRG
                WRG = Temp
                TempE = WG
                WG = OG
                OG = YG
                YG = RG
                RG = TempE
                C.EastC()
            if s == "y":
                for i in range(20):
                    Positive(Y,YRB,YR,YRG,YB,YG,YOB,YO,YOG,(0,1,0))
                    time += 1
                    rate(RATE)
                Temp = YRG
                YRG = YOG
                YOG = YOB
                YOB = YRB
                YRB = Temp
                TempE = YR
                YR = YG
                YG = YO
                YO = YB
                YB = TempE
                C.BottomC()
            if s == "Y":
                for i in range(20):
                    Negative(Y,YRB,YR,YRG,YB,YG,YOB,YO,YOG,(0,1,0))
                    time += 1
                    rate(RATE)
                Temp = YRG
                YRG = YRB
                YRB = YOB
                YOB = YOG
                YOG = Temp
                TempE = YG
                YG = YR
                YR = YB
                YB = YO
                YO = TempE
                C.BottomCC()
            if s == "R":
                for i in range(20):
                    Positive(R,WRB,YR,WRG,WR,RB,YRB,RG,YRG,(1,0,0))
                    time += 1
                    rate(RATE)
                Temp = WRB
                WRB = YRB
                YRB = YRG
                YRG = WRG
                WRG = Temp
                TempE = WR
                WR = RB
                RB = YR
                YR = RG
                RG = TempE
                C.NorthCC()
            if s == "r":
                for i in range(20):
                    Negative(R,WRB,YR,WRG,WR,RB,YRB,RG,YRG,(1,0,0))
                    time += 1
                    rate(RATE)
                Temp = WRB
                WRB = WRG
                WRG = YRG
                YRG = YRB
                YRB = Temp
                TempE = WR
                WR = RG
                RG = YR
                YR = RB
                RB = TempE
                C.NorthC()
            if s == "o":
                for i in range(20):
                    Positive(O,WOB,YO,WOG,WO,OB,YOB,OG,YOG,(1,0,0))
                    time += 1
                    rate(RATE)
                Temp = WOB
                WOB = YOB
                YOB = YOG
                YOG = WOG
                WOG = Temp
                TempE = WO
                WO = OB
                OB = YO
                YO = OG
                OG = TempE
                C.SouthC()
            if s == "O":
                for i in range(20):
                    Negative(O,WOB,YO,WOG,WO,OB,YOB,OG,YOG,(1,0,0))
                    time += 1
                    rate(RATE)
                Temp = WOB
                WOB = WOG
                WOG = YOG
                YOG = YOB
                YOB = Temp
                TempE = WO
                WO = OG
                OG = YO
                YO = OB
                OB = TempE
                C.SouthCC()
                """
            if s == "m":
                if Teach == False:                   
                    C.MixUp()
                    r = RATE
                    RATE = 200
                    rate(RATE)
                    for i in range(len(C.MixedSteps)):
                        if C.MixedSteps[i] == 'White Clockwise':
                            for i in range(20):
                                Negative(W,WRB,WR,WRG,WB,WG,WOB,WO,WOG,(0,1,0))
                                time += 1
                                rate(RATE)
                            Temp = WRG
                            WRG = WRB
                            WRB = WOB
                            WOB = WOG
                            WOG = Temp
                            TempE = WG
                            WG = WR
                            WR = WB
                            WB = WO
                            WO = TempE
                        elif C.MixedSteps[i] == 'White CounterClockwise':
                            for i in range(20):
                                Positive(W,WRB,WR,WRG,WB,WG,WOB,WO,WOG,(0,1,0))
                                time += 1
                                rate(RATE)
                            Temp = WRG
                            WRG = WOG
                            WOG = WOB
                            WOB = WRB
                            WRB = Temp
                            TempE = WR
                            WR = WG
                            WG = WO
                            WO = WB
                            WB = TempE
                        elif C.MixedSteps[i] == 'Blue Clockwise':
                            for i in range(20):
                                Positive(B,WRB,YB,YRB,WB,RB,WOB,OB,YOB,(0,0,1))
                                time += 1
                                rate(RATE)
                            Temp = WOB
                            WOB = WRB
                            WRB = YRB
                            YRB = YOB
                            YOB = Temp
                            TempE = WB
                            WB = RB
                            RB = YB
                            YB = OB
                            OB = TempE
                        elif C.MixedSteps[i] == 'Blue CounterClockwise':
                            for i in range(20):
                                Negative(B,WRB,YB,YRB,WB,RB,WOB,OB,YOB,(0,0,1))
                                time += 1
                                rate(RATE)
                            Temp = WOB
                            WOB = YOB
                            YOB = YRB
                            YRB = WRB
                            WRB = Temp
                            TempE = WB
                            WB = OB
                            OB = YB
                            YB = RB
                            RB = TempE
                        elif C.MixedSteps[i] == 'Green CounterClockwise':
                            for i in range(20):
                                Positive(G,WRG,YG,YRG,WG,RG,WOG,OG,YOG,(0,0,1))
                                time += 1
                                rate(RATE)
                            Temp = WOG
                            WOG = WRG
                            WRG = YRG
                            YRG = YOG
                            YOG = Temp
                            TempE = WG
                            WG = RG
                            RG = YG
                            YG = OG
                            OG = TempE
                        elif C.MixedSteps[i] == 'Green Clockwise':
                            for i in range(20):
                                Negative(G,WRG,YG,YRG,WG,RG,WOG,OG,YOG,(0,0,1))
                                time += 1
                                rate(RATE)
                            Temp = WOG
                            WOG = YOG
                            YOG = YRG
                            YRG = WRG
                            WRG = Temp
                            TempE = WG
                            WG = OG
                            OG = YG
                            YG = RG
                            RG = TempE
                        elif C.MixedSteps[i] == 'Yellow Clockwise':
                            for i in range(20):
                                Positive(Y,YRB,YR,YRG,YB,YG,YOB,YO,YOG,(0,1,0))
                                time += 1
                                rate(RATE)
                            Temp = YRG
                            YRG = YOG
                            YOG = YOB
                            YOB = YRB
                            YRB = Temp
                            TempE = YR
                            YR = YG
                            YG = YO
                            YO = YB
                            YB = TempE
                        elif C.MixedSteps[i] == 'Yellow CounterClockwise':
                            for i in range(20):
                                Negative(Y,YRB,YR,YRG,YB,YG,YOB,YO,YOG,(0,1,0))
                                time += 1
                                rate(RATE)
                            Temp = YRG
                            YRG = YRB
                            YRB = YOB
                            YOB = YOG
                            YOG = Temp
                            TempE = YG
                            YG = YR
                            YR = YB
                            YB = YO
                            YO = TempE
                        elif C.MixedSteps[i] == 'Red CounterClockwise':
                            for i in range(20):
                                Positive(R,WRB,YR,WRG,WR,RB,YRB,RG,YRG,(1,0,0))
                                time += 1
                                rate(RATE)
                            Temp = WRB
                            WRB = YRB
                            YRB = YRG
                            YRG = WRG
                            WRG = Temp
                            TempE = WR
                            WR = RB
                            RB = YR
                            YR = RG
                            RG = TempE
                        elif C.MixedSteps[i] == 'Red Clockwise':
                            for i in range(20):
                                Negative(R,WRB,YR,WRG,WR,RB,YRB,RG,YRG,(1,0,0))
                                time += 1
                                rate(RATE)
                            Temp = WRB
                            WRB = WRG
                            WRG = YRG
                            YRG = YRB
                            YRB = Temp
                            TempE = WR
                            WR = RG
                            RG = YR
                            YR = RB
                            RB = TempE
                        elif C.MixedSteps[i] == 'Orange Clockwise':
                            for i in range(20):
                                Positive(O,WOB,YO,WOG,WO,OB,YOB,OG,YOG,(1,0,0))
                                time += 1
                                rate(RATE)
                            Temp = WOB
                            WOB = YOB
                            YOB = YOG
                            YOG = WOG
                            WOG = Temp
                            TempE = WO
                            WO = OB
                            OB = YO
                            YO = OG
                            OG = TempE
                        elif C.MixedSteps[i] == 'Orange CounterClockwise':
                            for i in range(20):
                                Negative(O,WOB,YO,WOG,WO,OB,YOB,OG,YOG,(1,0,0))
                                time += 1
                                rate(RATE)
                            Temp = WOB
                            WOB = WOG
                            WOG = YOG
                            YOG = YOB
                            YOB = Temp
                            TempE = WO
                            WO = OG
                            OG = YO
                            YO = OB
                            OB = TempE
                        else:
                            print "Not a move"
                    RATE = r
                    


            if s == "s":
                Teach = True
                scene.forward = vector(-.1,-.1,-.1)
                BadImport = False
                if(C.WhiteCross() == False):
                    BadImport = True

                C.Solution += ['Corners']
                if (C.WhiteCorners() == False):
                    BadImport = True
                C.Solution += ['Two']
                if (C.StepTwo() == False):
                    BadImport == True
                C.Solution += ['Three']
                if (C.StepThree() == False):
                    BadImport = True
                C.Solution += ['Four']
                if (C.StepFour() == False):
                    BadImport = True
                C.Solution += ['Five']
                if (C.StepFive() == False):
                    BadImport = True
                C.Solution += ['Six']
                if (C.StepSix() == False):
                    BadImport = True
                C.CleanSolution()
                Moves = 0
                if Teach:
                    RATE = 10
                else:
                    RATE = 2500
                #k = scene.kb.getkey()
                if (BadImport):
                    T.text = 'Cube is not solvable'
                    scene.waitfor('keydown')
                    T.text = ''
                else:
                    Pointers = []
                    for i in range(len(C.Solution)):
                        Moves += 1
                        if Teach:
                            if scene.forward[0] > 0:
                                if scene.forward[2] > 0: 
                                    T.axis = (-1,0,1)
                                else:
                                    T.axis = (1,0,1)
                            else:
                                if scene.forward[2] > 0: 
                                    T.axis = (-1,0,-1)
                                else:
                                    T.axis = (1,0,-1)
                            if scene.forward[1] > 0:
                                T.pos = (0,-20,0)
                            else:
                                T.pos = (0,20,0)
                            if 'Clock' in C.Solution[i]:
                                T.text = C.Solution[i]
                                scene.waitfor('keydown')
                                for n in range(len(Pointers)):
                                    Pointers[0].f.visible = False
                                    del Pointers[0]
                            else:
                                T.text = ''
                            
                        if C.Solution[i] == 'White Clockwise':
                            for i in range(20):
                                Negative(W,WRB,WR,WRG,WB,WG,WOB,WO,WOG,(0,1,0))
                                time += 1
                                rate(RATE)
                            Temp = WRG
                            WRG = WRB
                            WRB = WOB
                            WOB = WOG
                            WOG = Temp
                            TempE = WG
                            WG = WR
                            WR = WB
                            WB = WO
                            WO = TempE
                        elif C.Solution[i] == 'White CounterClockwise':
                            for i in range(20):
                                Positive(W,WRB,WR,WRG,WB,WG,WOB,WO,WOG,(0,1,0))
                                time += 1
                                rate(RATE)
                            Temp = WRG
                            WRG = WOG
                            WOG = WOB
                            WOB = WRB
                            WRB = Temp
                            TempE = WR
                            WR = WG
                            WG = WO
                            WO = WB
                            WB = TempE
                        elif C.Solution[i] == 'Blue Clockwise':
                            for i in range(20):
                                Positive(B,WRB,YB,YRB,WB,RB,WOB,OB,YOB,(0,0,1))
                                time += 1
                                rate(RATE)
                            Temp = WOB
                            WOB = WRB
                            WRB = YRB
                            YRB = YOB
                            YOB = Temp
                            TempE = WB
                            WB = RB
                            RB = YB
                            YB = OB
                            OB = TempE
                        elif C.Solution[i] == 'Blue CounterClockwise':
                            for i in range(20):
                                Negative(B,WRB,YB,YRB,WB,RB,WOB,OB,YOB,(0,0,1))
                                time += 1
                                rate(RATE)
                            Temp = WOB
                            WOB = YOB
                            YOB = YRB
                            YRB = WRB
                            WRB = Temp
                            TempE = WB
                            WB = OB
                            OB = YB
                            YB = RB
                            RB = TempE
                        elif C.Solution[i] == 'Green CounterClockwise':
                            for i in range(20):
                                Positive(G,WRG,YG,YRG,WG,RG,WOG,OG,YOG,(0,0,1))
                                time += 1
                                rate(RATE)
                            Temp = WOG
                            WOG = WRG
                            WRG = YRG
                            YRG = YOG
                            YOG = Temp
                            TempE = WG
                            WG = RG
                            RG = YG
                            YG = OG
                            OG = TempE
                        elif C.Solution[i] == 'Green Clockwise':
                            for i in range(20):
                                Negative(G,WRG,YG,YRG,WG,RG,WOG,OG,YOG,(0,0,1))
                                time += 1
                                rate(RATE)
                            Temp = WOG
                            WOG = YOG
                            YOG = YRG
                            YRG = WRG
                            WRG = Temp
                            TempE = WG
                            WG = OG
                            OG = YG
                            YG = RG
                            RG = TempE
                        elif C.Solution[i] == 'Yellow ClockWise':
                            for i in range(20):
                                Positive(Y,YRB,YR,YRG,YB,YG,YOB,YO,YOG,(0,1,0))
                                time += 1
                                rate(RATE)
                            Temp = YRG
                            YRG = YOG
                            YOG = YOB
                            YOB = YRB
                            YRB = Temp
                            TempE = YR
                            YR = YG
                            YG = YO
                            YO = YB
                            YB = TempE
                        elif C.Solution[i] == 'Yellow CounterClockwise':
                            for i in range(20):
                                Negative(Y,YRB,YR,YRG,YB,YG,YOB,YO,YOG,(0,1,0))
                                time += 1
                                rate(RATE)
                            Temp = YRG
                            YRG = YRB
                            YRB = YOB
                            YOB = YOG
                            YOG = Temp
                            TempE = YG
                            YG = YR
                            YR = YB
                            YB = YO
                            YO = TempE
                        elif C.Solution[i] == 'Red CounterClockwise':
                            for i in range(20):
                                Positive(R,WRB,YR,WRG,WR,RB,YRB,RG,YRG,(1,0,0))
                                time += 1
                                rate(RATE)
                            Temp = WRB
                            WRB = YRB
                            YRB = YRG
                            YRG = WRG
                            WRG = Temp
                            TempE = WR
                            WR = RB
                            RB = YR
                            YR = RG
                            RG = TempE
                        elif C.Solution[i] == 'Red Clockwise':
                            for i in range(20):
                                Negative(R,WRB,YR,WRG,WR,RB,YRB,RG,YRG,(1,0,0))
                                time += 1
                                rate(RATE)
                            Temp = WRB
                            WRB = WRG
                            WRG = YRG
                            YRG = YRB
                            YRB = Temp
                            TempE = WR
                            WR = RG
                            RG = YR
                            YR = RB
                            RB = TempE
                        elif C.Solution[i] == 'Orange Clockwise':
                            for i in range(20):
                                Positive(O,WOB,YO,WOG,WO,OB,YOB,OG,YOG,(1,0,0))
                                time += 1
                                rate(RATE)
                            Temp = WOB
                            WOB = YOB
                            YOB = YOG
                            YOG = WOG
                            WOG = Temp
                            TempE = WO
                            WO = OB
                            OB = YO
                            YO = OG
                            OG = TempE
                        elif C.Solution[i] == 'Orange CounterClockwise':
                            for i in range(20):
                                Negative(O,WOB,YO,WOG,WO,OB,YOB,OG,YOG,(1,0,0))
                                time += 1
                                rate(RATE)
                            Temp = WOB
                            WOB = WOG
                            WOG = YOG
                            YOG = YOB
                            YOB = Temp
                            TempE = WO
                            WO = OG
                            OG = YO
                            YO = OB
                            OB = TempE
                        else:
                            Moves = Moves - 1
                            if Teach:
                                if 'piece' in C.Solution[i]:
                                    piece = C.Solution[i]
                                    if '0' in C.Solution[i]:
                                        vecs = edge(piece[6],piece[8],piece[10])
                                        Pointer1 = Pointer( vecs[0] )
                                        if vecs[0][0] > 7 or vecs[0][0] < -7:
                                            Pointer1.f.rotate(angle=pi/2,axis=(0,0,1), origin=Pointer1.f.pos)
                                        elif vecs[0][2] > 7 or vecs[0][2] < -7:
                                            Pointer1.f.rotate(angle=pi/2,axis=(1,0,0), origin=Pointer1.f.pos)

                                        Pointers += [Pointer1]

                                        Pointer2 = Pointer( vecs[1] )
                                        if vecs[1][0] > 7 or vecs[1][0] < -7:
                                            Pointer2.f.rotate(angle=pi/2,axis=(0,0,1), origin=Pointer2.f.pos)
                                        elif vecs[1][2] > 7 or vecs[1][2] < -7:
                                            Pointer2.f.rotate(angle=pi/2,axis=(1,0,0), origin=Pointer2.f.pos)
                                        Pointers += [Pointer2]


                                    else:
                                        vecs = corner(piece[6],piece[8],piece[10])
                                        Pointer1 = Pointer( vecs[0] )
                                        if vecs[0][0] > 7 or vecs[0][0] < -7:
                                            Pointer1.f.rotate(angle=pi/2,axis=(0,0,1), origin=Pointer1.f.pos)
                                        elif vecs[0][2] > 7 or vecs[0][2] < -7:
                                            Pointer1.f.rotate(angle=pi/2,axis=(1,0,0), origin=Pointer1.f.pos)

                                        Pointers += [Pointer1]

                                        Pointer2 = Pointer( vecs[1] )
                                        if vecs[1][0] > 7 or vecs[1][0] < -7:
                                            Pointer2.f.rotate(angle=pi/2,axis=(0,0,1), origin=Pointer2.f.pos)
                                        elif vecs[1][2] > 7 or vecs[1][2] < -7:
                                            Pointer2.f.rotate(angle=pi/2,axis=(1,0,0), origin=Pointer2.f.pos)
                                        Pointers += [Pointer2]

                                        Pointer3 = Pointer( vecs[2] )
                                        if vecs[2][0] > 7 or vecs[2][0] < -7:
                                            Pointer3.f.rotate(angle=pi/2,axis=(0,0,1), origin=Pointer3.f.pos)
                                        elif vecs[2][2] > 7 or vecs[2][2] < -7:
                                            Pointer3.f.rotate(angle=pi/2,axis=(1,0,0), origin=Pointer3.f.pos)
                                        Pointers += [Pointer3]

                                if 'move' in C.Solution[i]:
                                    move = C.Solution[i]
                                    moves = MoveTo(scene.forward[0],scene.forward[1],scene.forward[2],eval(move[5]),eval(move[7]),eval(move[9]))
                                    print moves
                                    for j in range(len(moves)):
                                        x = scene.forward[0]
                                        y = scene.forward[1]
                                        z = scene.forward[2]
                                        if moves[j] == 'up':
                                            for k in range(1,11):
                                                scene.forward = (x,y - .1155*k,z)
                                                rate(12)

                                        elif moves[j] == 'down':
                                            for k in range(1,11):
                                                scene.forward = (x,y + .1155*k,z)
                                                rate(12)

                                        elif moves[j] == 'xminus':
                                            if z > 0:
                                                for k in range(1,11):
                                                    scene.forward = (x-.1155*k,y,(1-y**2-(x-.1155*k)**2)**(0.5))
                                                    rate(12)
                                            else:
                                                for k in range(1,11):
                                                    scene.forward = (x-.1155*k,y,-(1-y**2-(x-.1155*k)**2)**(0.5))
                                                    rate(12)

                                        elif moves[j] == 'xplus':
                                            if z > 0:
                                                for k in range(1,11):
                                                    scene.forward = (x+.1155*k,y,(1-y**2-(x+.1155*k)**2)**(0.5))
                                                    rate(12)
                                            else:
                                                for k in range(1,11):
                                                    scene.forward = (x+.1155*k,y,-(1-y**2-(x+.1155*k)**2)**(0.5))
                                                    rate(12)

                                        elif moves[j] == 'zplus':
                                            if x > 0:
                                                for k in range(1,11):
                                                    scene.forward = ((1-y**2-(z+.1155*k)**2)**(0.5),y,z+.1155*k)
                                                    rate(12)
                                            else:
                                                for k in range(1,11):
                                                    scene.forward = (-(1-y**2-(z+.1155*k)**2)**(0.5),y,z+.1155*k)
                                                    rate(12)

                                        elif moves[j] == 'zminus':
                                            if x > 0:
                                                for k in range(1,11):
                                                    scene.forward = ((1-y**2-(z-.1155*k)**2)**(0.5),y,z-.1155*k)
                                                    rate(12)
                                            else:
                                                for k in range(1,11):
                                                    scene.forward = (-(1-y**2-(z-.1155*k)**2)**(0.5),y,z-.1155*k)
                                                    rate(12)
                print Moves
                T.text = ""
                T.pos = T.pos = (0,20,0)
                Teach = False

                                    

                
            
            if s == "1":
                scene.forward = vector(-.1,-.1,-.1)
                for i in range(10):
                    move = 'move '
                    move += createPorN() + ' '
                    move += createPorN() + ' '
                    move += createPorN()
                    C.Solution += [move]
                print C.Solution
                for i in range(len(C.Solution)):
                    if 'move' in C.Solution[i]:
                        move = C.Solution[i]
                        moves = MoveTo(scene.forward[0],scene.forward[1],scene.forward[2],eval(move[5]),eval(move[7]),eval(move[9]))

                        for j in range(len(moves)):
                            x = scene.forward[0]
                            y = scene.forward[1]
                            z = scene.forward[2]
                            if moves[j] == 'up':
                                for k in range(1,11):
                                    scene.forward = (x,y - .1155*k,z)
                                    rate(12)

                            elif moves[j] == 'down':
                                for k in range(1,11):
                                    scene.forward = (x,y + .1155*k,z)
                                    rate(12)

                            elif moves[j] == 'xminus':
                                if z > 0:
                                    for k in range(1,11):
                                        scene.forward = (x-.1155*k,y,(1-y**2-(x-.1155*k)**2)**(0.5))
                                        rate(12)
                                else:
                                    for k in range(1,11):
                                        scene.forward = (x-.1155*k,y,-(1-y**2-(x-.1155*k)**2)**(0.5))
                                        rate(12)

                            elif moves[j] == 'xplus':
                                if z > 0:
                                    for k in range(1,11):
                                        scene.forward = (x+.1155*k,y,(1-y**2-(x+.1155*k)**2)**(0.5))
                                        rate(12)
                                else:
                                    for k in range(1,11):
                                        scene.forward = (x+.1155*k,y,-(1-y**2-(x+.1155*k)**2)**(0.5))
                                        rate(12)

                            elif moves[j] == 'zplus':
                                if x > 0:
                                    for k in range(1,11):
                                        scene.forward = ((1-y**2-(z+.1155*k)**2)**(0.5),y,z+.1155*k)
                                        rate(12)
                                else:
                                    for k in range(1,11):
                                        scene.forward = (-(1-y**2-(z+.1155*k)**2)**(0.5),y,z+.1155*k)
                                        rate(12)

                            elif moves[j] == 'zminus':
                                if x > 0:
                                    for k in range(1,11):
                                        scene.forward = ((1-y**2-(z-.1155*k)**2)**(0.5),y,z-.1155*k)
                                        rate(12)
                                else:
                                    for k in range(1,11):
                                        scene.forward = (-(1-y**2-(z-.1155*k)**2)**(0.5),y,z-.1155*k)
                                        rate(12)

def eval(n):
    if n == 'p':
        return 1
    else:
        return -1

def createPorN():
    n = random.randint(0,2)
    if n == 0:
        return 'p'
    else:
        return 'n'

def MoveTo(x1,y1,z1,x2,y2,z2):
    moves = []
    if y1 > 0 and y2 < 0:
        moves += ['up']
    if y1 < 0 and y2 > 0:
        moves += ['down']

    if x1 > 0 and x2 < 0:
        moves += ['xminus']
    if x1 < 0 and x2 > 0:
        moves += ['xplus']

    if z1 > 0 and z2 < 0:
        moves += ['zminus']
    if z1 < 0 and z2 > 0:
        moves += ['zplus']

    return moves

def corner(x,y,z):
    vecs = []

    a = 0
    b = 0
    c = 0
    if x == 'p':
        a = 5.2
    else:
        a = -5.2

    if y == 'p':
        b = 5.2
    else:
        b = -5.2

    if z == 'p':
        c = 7.7
    else:
        c = -7.7

    vecs += [(a,b,c)]

    if x == 'p':
        a = 5.2
    else:
        a = -5.2

    if y == 'p':
        b = 7.7
    else:
        b = -7.7

    if z == 'p':
        c = 5.2
    else:
        c = -5.2

    vecs += [(a,b,c)]

    if x == 'p':
        a = 7.7
    else:
        a = -7.7

    if y == 'p':
        b = 5.2
    else:
        b = -5.2

    if z == 'p':
        c = 5.2
    else:
        c = -5.2

    vecs += [(a,b,c)]

    return vecs



def edge(x,y,z):
    vecs = []

    a = 0
    b = 0
    c = 0

    if x == '0':
        a = 0
        if y == 'p':
            b = 5.2
        else:
            b = -5.2

        if z == 'p':
            c = 7.7
        else:
            c = -7.7
        vecs += [(a,b,c)]

        if y == 'p':
            b = 7.7
        else:
            b = -7.7

        if z == 'p':
            c = 5.2
        else:
            c = -5.2
        vecs += [(a,b,c)]

    elif y == '0':
        b = 0
        if x == 'p':
            a = 5.2
        else:
            a = -5.2

        if z == 'p':
            c = 7.7
        else:
            c = -7.7
        vecs += [(a,b,c)]

        if x == 'p':
            a = 7.7
        else:
            a = -7.7

        if z == 'p':
            c = 5.2
        else:
            c = -5.2
        vecs += [(a,b,c)]

    else:
        c = 0
        if x == 'p':
            a = 5.2
        else:
            a = -5.2

        if y == 'p':
            b = 7.7
        else:
            b = -7.7
        vecs += [(a,b,c)]

        if x == 'p':
            a = 7.7
        else:
            a = -7.7

        if y == 'p':
            b = 5.2
        else:
            b = -5.2
        vecs += [(a,b,c)]

    return vecs



if __name__ == "__main__":
    main()






