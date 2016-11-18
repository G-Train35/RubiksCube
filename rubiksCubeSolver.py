import random


class cube:          
        
    # first is Top
    TopN = ('W','R') 
    TopE = ('W','G')
    TopS = ('W','O')
    TopW = ('W','B')

    # first is Bottom
    BottomN = ('Y','R')
    BottomE = ('Y','G')
    BottomS = ('Y','O')
    BottomW = ('Y','B')

    # first is either North or South
    MiddleNE = ('R','G')
    MiddleNW = ('R','B')
    MiddleSE = ('O','G')
    MiddleSW = ('O','B')

    # first is Top, then order of name 
    TopNE = ('W','R','G')
    TopNW = ('W','R','B')
    TopSE = ('W','O','G')
    TopSW = ('W','O','B')

    # first is Bottom, then order of name 
    BottomNE = ('Y','R','G')
    BottomNW = ('Y','R','B')
    BottomSE = ('Y','O','G')
    BottomSW = ('Y','O','B')

    # the list of MixUp
    MixedSteps = []

    # the list of steps for solution
    Solution = []
    Add = False


    def PrintCube(self):
       print '             Top'
       print '              -----------'
       print '             | ' + self.TopNW[0] + ' | ' + self.TopN[0] + ' | ' + self.TopNE[0] + ' |'
       print '              -----------'
       print '             | ' + self.TopW[0] + ' | W | ' + self.TopE[0] + ' |'
       print '              -----------'
       print '             | ' + self.TopSW[0] + ' | ' + self.TopS[0] + ' | ' + self.TopSE[0] + ' |'
       print '              -----------'

       print 'Left         ' + 'Front            ' + 'Right'
       print ' ----------- ' + ' ----------- ' + ' ----------- '
       print '| ' + self.TopNW[2] + ' | ' + self.TopW[1] + ' | ' + self.TopSW[2] + ' |' + '| ' + self.TopSW[1] + ' | ' + self.TopS[1] + ' | ' + self.TopSE[1] + ' |' + '| ' + self.TopSE[2] + ' | ' + self.TopE[1] + ' | ' + self.TopNE[2] + ' |'
       print ' ----------- ' + ' ----------- ' + ' ----------- '
       print '| ' + self.MiddleNW[1] + ' | B | ' + self.MiddleSW[1] + ' |' + '| ' + self.MiddleSW[0] + ' | O | ' + self.MiddleSE[0] + ' |' + '| ' + self.MiddleSE[1] + ' | G | ' + self.MiddleNE[1] + ' |'
       print ' ----------- ' + ' ----------- ' + ' ----------- '
       print '| ' + self.BottomNW[2] + ' | ' + self.BottomW[1] + ' | ' + self.BottomSW[2] + ' |' + '| ' + self.BottomSW[1] + ' | ' + self.BottomS[1] + ' | ' + self.BottomSE[1] + ' |' + '| ' + self.BottomSE[2] + ' | ' + self.BottomE[1] + ' | ' + self.BottomNE[2] + ' |'
       print ' ----------- ' + ' ----------- ' + ' ----------- '
       
       print '             Bottom'
       print '              -----------'
       print '             | ' + self.BottomSW[0] + ' | ' + self.BottomS[0] + ' | ' + self.BottomSE[0] + ' |'
       print '              -----------'
       print '             | ' + self.BottomW[0] + ' | Y | ' + self.BottomE[0] + ' |'
       print '              -----------'
       print '             | ' + self.BottomNW[0] + ' | ' + self.BottomN[0] + ' | ' + self.BottomNE[0] + ' |'
       print '              -----------'

       print 'Back'
       print ' -----------'
       print '| ' + self.TopNE[1] + ' | ' + self.TopN[1] + ' | ' + self.TopNW[1] + ' |'
       print ' -----------'
       print '| ' + self.MiddleNE[0] + ' | R | ' + self.MiddleNW[0] + ' |'
       print ' -----------'
       print '| ' + self.BottomNE[1] + ' | ' + self.BottomN[1] + ' | ' + self.BottomNW[1] + ' |'
       print ' -----------'


    def MixUp(self):
        self.MixedSteps = []
        for i in range(25):
            x = int(random.uniform(1,13))
            if x == 1:
                self.TopC()
                self.MixedSteps += ['White Clockwise']
            elif x == 2:
                self.TopCC()
                self.MixedSteps += ['White CounterClockwise']
            elif x == 3:
                self.BottomC()
                self.MixedSteps += ['Yellow Clockwise']
            elif x == 4:
                self.BottomCC()
                self.MixedSteps += ['Yellow CounterClockwise']
            elif x == 5:
                self.WestC()
                self.MixedSteps += ['Blue Clockwise']
            elif x == 6:
                self.WestCC()
                self.MixedSteps += ['Blue CounterClockwise']
            elif x == 7:
                self.NorthC()
                self.MixedSteps += ['Red Clockwise']
            elif x == 8:
                self.NorthCC()
                self.MixedSteps += ['Red CounterClockwise']
            elif x == 9:
                self.SouthC()
                self.MixedSteps += ['Orange Clockwise']
            elif x == 10:
                self.SouthCC()
                self.MixedSteps += ['Orange CounterClockwise']
            elif x == 11:
                self.EastC()
                self.MixedSteps += ['Green Clockwise']
            else:
                self.EastCC()
                self.MixedSteps += ['Green CounterClockwise']

    
    def TopC(self):
        if self.Add:
            self.Solution += ['White Clockwise']
        TempN = self.TopN
        TempW = self.TopW
        TempS = self.TopS
        TempE = self.TopE
        
        TempNE = self.TopNE
        TempNW = self.TopNW
        TempSW = self.TopSW
        TempSE = self.TopSE

        
        self.TopN = TempW
        self.TopE = TempN
        self.TopS = TempE
        self.TopW = TempS
        
        self.TopNE = (TempNW[0],TempNW[2],TempNW[1])
        self.TopNW = (TempSW[0],TempSW[2],TempSW[1])
        self.TopSE = (TempNE[0],TempNE[2],TempNE[1])
        self.TopSW = (TempSE[0],TempSE[2],TempSE[1])

    def CopyTopC(self):
        TempN = self.TopN
        TempW = self.TopW
        TempS = self.TopS
        TempE = self.TopE
        
        TempNE = self.TopNE
        TempNW = self.TopNW
        TempSW = self.TopSW
        TempSE = self.TopSE

        
        self.TopN = TempW
        self.TopE = TempN
        self.TopS = TempE
        self.TopW = TempS
        
        self.TopNE = (TempNW[0],TempNW[2],TempNW[1])
        self.TopNW = (TempSW[0],TempSW[2],TempSW[1])
        self.TopSE = (TempNE[0],TempNE[2],TempNE[1])
        self.TopSW = (TempSE[0],TempSE[2],TempSE[1])

    def TopCC(self):
       if self.Add:
           self.Solution += ['White CounterClockwise']
       self.CopyTopC()
       self.CopyTopC()
       self.CopyTopC()

    def BottomCC(self):
       if self.Add:
           self.Solution += ['Yellow CounterClockwise']
       self.CopyBottomC()
       self.CopyBottomC()
       self.CopyBottomC()

    def BottomC(self):
       if self.Add:
           self.Solution += ['Yellow ClockWise']
       TempN = self.BottomN
       TempW = self.BottomW
       TempS = self.BottomS
       TempE = self.BottomE
       
       TempNE = self.BottomNE
       TempNW = self.BottomNW
       TempSW = self.BottomSW
       TempSE = self.BottomSE

        
       self.BottomN = TempE
       self.BottomE = TempS
       self.BottomS = TempW
       self.BottomW = TempN
       
       self.BottomNE = (TempSE[0],TempSE[2],TempSE[1])
       self.BottomNW = (TempNE[0],TempNE[2],TempNE[1])
       self.BottomSE = (TempSW[0],TempSW[2],TempSW[1])
       self.BottomSW = (TempNW[0],TempNW[2],TempNW[1])

    def CopyBottomC(self):
       TempN = self.BottomN
       TempW = self.BottomW
       TempS = self.BottomS
       TempE = self.BottomE
       
       TempNE = self.BottomNE
       TempNW = self.BottomNW
       TempSW = self.BottomSW
       TempSE = self.BottomSE

        
       self.BottomN = TempE
       self.BottomE = TempS
       self.BottomS = TempW
       self.BottomW = TempN
       
       self.BottomNE = (TempSE[0],TempSE[2],TempSE[1])
       self.BottomNW = (TempNE[0],TempNE[2],TempNE[1])
       self.BottomSE = (TempSW[0],TempSW[2],TempSW[1])
       self.BottomSW = (TempNW[0],TempNW[2],TempNW[1])


    def NorthC(self):
       if self.Add:
           self.Solution += ['Red Clockwise']
       TempTopN = self.TopN
       TempBottomN = self.BottomN
       TempMidNE = self.MiddleNE
       TempMidNW = self.MiddleNW

       TempTopNE = self.TopNE
       TempTopNW = self.TopNW
       TempBottomNW = self.BottomNW
       TempBottomNE = self.BottomNE

        
       self.TopN = TempMidNE[::-1]
       self.MiddleNE = TempBottomN[::-1]
       self.BottomN = TempMidNW[::-1]
       self.MiddleNW = TempTopN[::-1]

       self.TopNE = TempBottomNE[::-1]
       self.TopNW = TempTopNE[::-1]
       self.BottomNW = TempTopNW[::-1]
       self.BottomNE = TempBottomNW[::-1]


    def CopyNorthC(self):
       TempTopN = self.TopN
       TempBottomN = self.BottomN
       TempMidNE = self.MiddleNE
       TempMidNW = self.MiddleNW

       TempTopNE = self.TopNE
       TempTopNW = self.TopNW
       TempBottomNW = self.BottomNW
       TempBottomNE = self.BottomNE

        
       self.TopN = TempMidNE[::-1]
       self.MiddleNE = TempBottomN[::-1]
       self.BottomN = TempMidNW[::-1]
       self.MiddleNW = TempTopN[::-1]

       self.TopNE = TempBottomNE[::-1]
       self.TopNW = TempTopNE[::-1]
       self.BottomNW = TempTopNW[::-1]
       self.BottomNE = TempBottomNW[::-1]

    def NorthCC(self):
       if self.Add:
           self.Solution += ['Red CounterClockwise']
       self.CopyNorthC()
       self.CopyNorthC()
       self.CopyNorthC()

    def SouthC(self):
       if self.Add:
           self.Solution += ['Orange Clockwise']
       TempTopS = self.TopS
       TempBottomS = self.BottomS
       TempMidSE = self.MiddleSE
       TempMidSW = self.MiddleSW

       TempTopSE = self.TopSE
       TempTopSW = self.TopSW
       TempBottomSW = self.BottomSW
       TempBottomSE = self.BottomSE

        
       self.TopS = TempMidSW[::-1]
       self.MiddleSE = TempTopS[::-1]
       self.BottomS = TempMidSE[::-1]
       self.MiddleSW = TempBottomS[::-1]

       self.TopSE = TempTopSW[::-1]
       self.TopSW = TempBottomSW[::-1]
       self.BottomSW = TempBottomSE[::-1]
       self.BottomSE = TempTopSE[::-1]


    def CopySouthC(self):
       TempTopS = self.TopS
       TempBottomS = self.BottomS
       TempMidSE = self.MiddleSE
       TempMidSW = self.MiddleSW

       TempTopSE = self.TopSE
       TempTopSW = self.TopSW
       TempBottomSW = self.BottomSW
       TempBottomSE = self.BottomSE

        
       self.TopS = TempMidSW[::-1]
       self.MiddleSE = TempTopS[::-1]
       self.BottomS = TempMidSE[::-1]
       self.MiddleSW = TempBottomS[::-1]

       self.TopSE = TempTopSW[::-1]
       self.TopSW = TempBottomSW[::-1]
       self.BottomSW = TempBottomSE[::-1]
       self.BottomSE = TempTopSE[::-1]

    def SouthCC(self):
       if self.Add:
           self.Solution += ['Orange CounterClockwise']
       self.CopySouthC()
       self.CopySouthC()
       self.CopySouthC()

    def EastC(self):
       if self.Add:
           self.Solution += ['Green Clockwise']
       TempTopE = self.TopE
       TempBottomE = self.BottomE
       TempMidSE = self.MiddleSE
       TempMidNE = self.MiddleNE

       TempTopSE = self.TopSE
       TempTopNE = self.TopNE
       TempBottomSE = self.BottomSE
       TempBottomNE = self.BottomNE

        
       self.TopE = TempMidSE
       self.MiddleSE = TempBottomE
       self.BottomE = TempMidNE
       self.MiddleNE = TempTopE

       self.TopSE = (TempBottomSE[1],TempBottomSE[0],TempBottomSE[2])
       self.TopNE = (TempTopSE[1],TempTopSE[0],TempTopSE[2])
       self.BottomNE = (TempTopNE[1],TempTopNE[0],TempTopNE[2])
       self.BottomSE = (TempBottomNE[1],TempBottomNE[0],TempBottomNE[2])

    def CopyEastC(self):
       TempTopE = self.TopE
       TempBottomE = self.BottomE
       TempMidSE = self.MiddleSE
       TempMidNE = self.MiddleNE

       TempTopSE = self.TopSE
       TempTopNE = self.TopNE
       TempBottomSE = self.BottomSE
       TempBottomNE = self.BottomNE

        
       self.TopE = TempMidSE
       self.MiddleSE = TempBottomE
       self.BottomE = TempMidNE
       self.MiddleNE = TempTopE

       self.TopSE = (TempBottomSE[1],TempBottomSE[0],TempBottomSE[2])
       self.TopNE = (TempTopSE[1],TempTopSE[0],TempTopSE[2])
       self.BottomNE = (TempTopNE[1],TempTopNE[0],TempTopNE[2])
       self.BottomSE = (TempBottomNE[1],TempBottomNE[0],TempBottomNE[2])

    def EastCC(self):
        if self.Add:
            self.Solution += ['Green CounterClockwise']
        self.CopyEastC()
        self.CopyEastC()
        self.CopyEastC()

    
    def WestC(self):
       if self.Add:
           self.Solution += ['Blue Clockwise']
       TempTopW = self.TopW
       TempBottomW = self.BottomW
       TempMidSW = self.MiddleSW
       TempMidNW = self.MiddleNW

       TempTopSW = self.TopSW
       TempTopNW = self.TopNW
       TempBottomSW = self.BottomSW
       TempBottomNW = self.BottomNW

        
       self.TopW = TempMidNW
       self.MiddleSW = TempTopW
       self.BottomW = TempMidSW
       self.MiddleNW = TempBottomW

       self.TopSW = (TempTopNW[1],TempTopNW[0],TempTopNW[2])
       self.TopNW = (TempBottomNW[1],TempBottomNW[0],TempBottomNW[2])
       self.BottomNW = (TempBottomSW[1],TempBottomSW[0],TempBottomSW[2])
       self.BottomSW = (TempTopSW[1],TempTopSW[0],TempTopSW[2])

    def CopyWestC(self):
       TempTopW = self.TopW
       TempBottomW = self.BottomW
       TempMidSW = self.MiddleSW
       TempMidNW = self.MiddleNW

       TempTopSW = self.TopSW
       TempTopNW = self.TopNW
       TempBottomSW = self.BottomSW
       TempBottomNW = self.BottomNW

        
       self.TopW = TempMidNW
       self.MiddleSW = TempTopW
       self.BottomW = TempMidSW
       self.MiddleNW = TempBottomW

       self.TopSW = (TempTopNW[1],TempTopNW[0],TempTopNW[2])
       self.TopNW = (TempBottomNW[1],TempBottomNW[0],TempBottomNW[2])
       self.BottomNW = (TempBottomSW[1],TempBottomSW[0],TempBottomSW[2])
       self.BottomSW = (TempTopSW[1],TempTopSW[0],TempTopSW[2])


    def WestCC(self):
        if self.Add:
            self.Solution += ['Blue CounterClockwise']
        self.CopyWestC()
        self.CopyWestC()
        self.CopyWestC()


    def Clockwise(self,C1,C2):
        if C1 == 'R' and C2 == 'G':
            return True
        if C1 == 'G' and C2 == 'O':
            return True
        if C1 == 'O' and C2 == 'B':
            return True
        if C1 == 'B' and C2 == 'R':
            return True
        return False

    def Opposites(self,C1,C2):
        if C1 == 'R' and C2 == 'O':
            return True
        if C1 == 'B' and C2 == 'G':
            return True
        if C1 == 'O' and C2 == 'R':
            return True
        if C1 == 'G' and C2 == 'B':
            return True
        return False

    def CleanSolution(self):
        i = 0
        while i < len(self.Solution)-2:
            if self.Solution[i] == self.Solution[i+1] and self.Solution[i+1] == self.Solution[i+2]:
                if 'CounterClockwise' in self.Solution[i]:
                    self.Solution[i] = self.Solution[i][0:len(self.Solution[i])-16] + 'Clockwise'
                else:
                    self.Solution[i] = self.Solution[i][0:len(self.Solution[i])-9] + 'CounterClockwise'
                    
                if i+3 == len(self.Solution):
                    self.Solution = self.Solution[0:i+1]
                else:
                    self.Solution = self.Solution[0:i+1] + self.Solution[i+3:]
            i += 1
                    
                    
            


    # algorithm 1

    def FirstFour(self):
        if self.MiddleNE[0] == 'W':
                self.Solution += ['piece p 0 p']
                self.Solution += ['move n n n']
                if self.TopN[0] == 'W':
                    if self.Clockwise(self.TopN[1],self.MiddleNE[1]):
                        self.EastCC()
                    elif self.Opposites(self.TopN[1],self.MiddleNE[1]):
                        self.TopCC()
                        self.EastCC()
                    else:
                        self.TopC()
                        self.TopC()
                        self.EastCC()
                elif self.TopW[0] == 'W':
                    if self.Clockwise(self.TopW[1],self.MiddleNE[1]):
                        self.TopC()
                        self.EastCC()
                    elif self.Opposites(self.TopW[1],self.MiddleNE[1]):
                        self.EastCC()
                    else:
                        self.TopCC()
                        self.EastCC()
                elif self.TopS[0] == 'W':
                    if self.Clockwise(self.TopS[1],self.MiddleNE[1]):
                        self.TopC()
                        self.TopC()
                        self.EastCC()
                    elif self.Opposites(self.TopS[1],self.MiddleNE[1]):
                        self.TopCC()
                        self.EastCC()
                    else:
                        self.EastCC()
                elif self.TopW[0] == 'W':
                    if self.Clockwise(self.TopW[1],self.MiddleNE[1]):
                        self.TopCC()
                        self.EastCC()
                    elif self.Opposites(self.TopW[1],self.MiddleNE[1]):
                        self.TopC()
                        self.TopC()
                        self.EastCC()
                    else:
                        self.TopC()
                        self.EastCC()
                else:
                    self.EastCC()

        elif self.MiddleNE[1] == 'W':
                self.Solution += ['piece p 0 p']
                self.Solution += ['move n n n']
                if self.TopN[0] == 'W':
                    if self.Clockwise(self.TopN[1],self.MiddleNE[0]):
                        self.TopCC()
                        self.NorthC()
                    elif self.Opposites(self.TopN[1],self.MiddleNE[0]):
                        self.TopC()
                        self.TopC()
                        self.NorthC()
                    else:
                        self.TopC()
                        self.NorthC()
                elif self.TopW[0] == 'W':
                    if self.Clockwise(self.TopW[1],self.MiddleNE[0]):
                        self.NorthC()
                    elif self.Opposites(self.TopW[1],self.MiddleNE[0]):
                        self.TopCC()
                        self.NorthC()
                    else:
                        self.TopC()
                        self.TopC()
                        self.NorthC()
                elif self.TopS[0] == 'W':
                    if self.Clockwise(self.TopS[1],self.MiddleNE[0]):
                        self.TopC()
                        self.NorthC()
                    elif self.Opposites(self.TopS[1],self.MiddleNE[0]):
                        self.NorthC()
                    else:
                        self.TopCC()
                        self.NorthC()
                elif self.TopW[0] == 'W':
                    if self.Clockwise(self.TopW[1],self.MiddleNE[0]):
                        self.TopC()
                        self.TopC()
                        self.NorthC()
                    elif self.Opposites(self.TopW[1],self.MiddleNE[0]):
                        self.TopC()
                        self.NorthC()
                    else:
                        self.NorthC()
                else:
                    self.NorthC()

        elif self.MiddleNW[1] == 'W':
                self.Solution += ['piece p 0 n']
                self.Solution += ['move n n p']
                if self.TopW[0] == 'W':
                    if self.Clockwise(self.TopW[1],self.MiddleNW[0]):
                        self.NorthCC()
                    elif self.Opposites(self.TopW[1],self.MiddleNW[0]):
                        self.TopCC()
                        self.NorthCC()
                    else:
                        self.TopC()
                        self.TopC()
                        self.NorthCC()
                elif self.TopS[0] == 'W':
                    if self.Clockwise(self.TopS[1],self.MiddleNW[0]):
                        self.TopC()
                        self.NorthCC()
                    elif self.Opposites(self.TopS[1],self.MiddleNW[0]):
                        self.NorthCC()
                    else:
                        self.TopCC()
                        self.NorthCC()
                elif self.TopE[0] == 'W':
                    if self.Clockwise(self.TopE[1],self.MiddleNW[0]):
                        self.TopC()
                        self.TopC()
                        self.NorthCC()
                    elif self.Opposites(self.TopE[1],self.MiddleNW[0]):
                        self.TopCC()
                        self.NorthCC()
                    else:
                        self.NorthCC()
                elif self.TopN[0] == 'W':
                    if self.Clockwise(self.TopN[1],self.MiddleNW[0]):
                        self.TopCC()
                        self.NorthCC()
                    elif self.Opposites(self.TopN[1],self.MiddleNW[0]):
                        self.TopC()
                        self.TopC()
                        self.NorthCC()
                    else:
                        self.TopC()
                        self.NorthCC()
                else:
                    self.NorthCC()

        elif self.MiddleNW[0] == 'W':
                self.Solution += ['piece p 0 n']
                self.Solution += ['move n n p']
                if self.TopW[0] == 'W':
                    if self.Clockwise(self.TopW[1],self.MiddleNW[1]):
                        self.TopCC()
                        self.WestC()
                    elif self.Opposites(self.TopW[1],self.MiddleNW[1]):
                        self.TopC()
                        self.TopC()
                        self.WestC()
                    else:
                        self.TopC()
                        self.WestC()
                elif self.TopS[0] == 'W':
                    if self.Clockwise(self.TopS[1],self.MiddleNW[1]):
                        self.WestC()
                    elif self.Opposites(self.TopS[1],self.MiddleNW[1]):
                        self.TopCC()
                        self.WestC()
                    else:
                        self.TopC()
                        self.TopC()
                        self.WestC()
                elif self.TopE[0] == 'W':
                    if self.Clockwise(self.TopE[1],self.MiddleNW[1]):
                        self.TopC()
                        self.WestC()
                    elif self.Opposites(self.TopE[1],self.MiddleNW[1]):
                        self.WestC()
                    else:
                        self.TopCC()
                        self.WestC()
                elif self.TopN[0] == 'W':
                    if self.Clockwise(self.TopN[1],self.MiddleNW[1]):
                        self.TopC()
                        self.TopC()
                        self.WestC()
                    elif self.Opposites(self.TopN[1],self.MiddleNW[1]):
                        self.TopC()
                        self.WestC()
                    else:
                        self.WestC()
                else:
                    self.WestC()

        elif self.MiddleSW[0] == 'W':
                self.Solution += ['piece n 0 n']
                self.Solution += ['move p n p']
                if self.TopS[0] == 'W':
                    if self.Clockwise(self.TopS[1],self.MiddleSW[1]):
                        self.WestCC()
                    elif self.Opposites(self.TopS[1],self.MiddleSW[1]):
                        self.TopCC()
                        self.WestCC()
                    else:
                        self.TopC()
                        self.TopC()
                        self.WestCC()
                elif self.TopE[0] == 'W':
                    if self.Clockwise(self.TopE[1],self.MiddleSW[1]):
                        self.TopC()
                        self.WestCC()
                    elif self.Opposites(self.TopE[1],self.MiddleSW[1]):
                        self.WestCC()
                    else:
                        self.TopCC()
                        self.WestCC()
                elif self.TopN[0] == 'W':
                    if self.Clockwise(self.TopN[1],self.MiddleSW[1]):
                        self.TopC()
                        self.TopC()
                        self.WestCC()
                    elif self.Opposites(self.TopN[1],self.MiddleSW[1]):
                        self.TopCC()
                        self.WestCC()
                    else:
                        self.WestCC()
                elif self.TopW[0] == 'W':
                    if self.Clockwise(self.TopW[1],self.MiddleSW[1]):
                        self.TopCC()
                        self.WestCC()
                    elif self.Opposites(self.TopW[1],self.MiddleSW[1]):
                        self.TopC()
                        self.TopC()
                        self.WestCC()
                    else:
                        self.TopC()
                        self.WestCC()
                else:
                    self.WestCC()

        elif self.MiddleSW[1] == 'W':
                self.Solution += ['piece n 0 n']
                self.Solution += ['move p n p']
                if self.TopS[0] == 'W':
                    if self.Clockwise(self.TopS[1],self.MiddleSW[0]):
                        self.TopCC()
                        self.SouthC()
                    elif self.Opposites(self.TopS[1],self.MiddleSW[0]):
                        self.TopC()
                        self.TopC()
                        self.SouthC()
                    else:
                        self.TopC()
                        self.SouthC()
                elif self.TopE[0] == 'W':
                    if self.Clockwise(self.TopE[1],self.MiddleSW[0]):
                        self.SouthC()
                    elif self.Opposites(self.TopE[1],self.MiddleSW[0]):
                        self.TopCC()
                        self.SouthC()
                    else:
                        self.TopC()
                        self.TopC()
                        self.SouthC()
                elif self.TopN[0] == 'W':
                    if self.Clockwise(self.TopN[1],self.MiddleSW[0]):
                        self.TopC()
                        self.SouthC()
                    elif self.Opposites(self.TopN[1],self.MiddleSW[0]):
                        self.SouthC()
                    else:
                        self.TopCC()
                        self.SouthC()
                elif self.TopW[0] == 'W':
                    if self.Clockwise(self.TopW[1],self.MiddleSW[0]):
                        self.TopC()
                        self.TopC()
                        self.SouthC()
                    elif self.Opposites(self.TopW[1],self.MiddleSW[0]):
                        self.TopC()
                        self.SouthC()
                    else:
                        self.SouthC()
                else:
                    self.SouthC()

        elif self.MiddleSE[1] == 'W':
                self.Solution += ['piece n 0 p']
                self.Solution += ['move p n n']
                if self.TopE[0] == 'W':
                    if self.Clockwise(self.TopE[1],self.MiddleSE[0]):
                        self.SouthCC()
                    elif self.Opposites(self.TopE[1],self.MiddleSE[0]):
                        self.TopCC()
                        self.SouthCC()
                    else:
                        self.TopC()
                        self.TopC()
                        self.SouthCC()
                elif self.TopN[0] == 'W':
                    if self.Clockwise(self.TopN[1],self.MiddleSE[0]):
                        self.TopC()
                        self.SouthCC()
                    elif self.Opposites(self.TopN[1],self.MiddleSE[0]):
                        self.SouthCC()
                    else:
                        self.TopCC()
                        self.SouthCC()
                elif self.TopW[0] == 'W':
                    if self.Clockwise(self.TopW[1],self.MiddleSE[0]):
                        self.TopC()
                        self.TopC()
                        self.SouthCC()
                    elif self.Opposites(self.TopW[1],self.MiddleSE[0]):
                        self.TopCC()
                        self.SouthCC()
                    else:
                        self.SouthCC()
                elif self.TopS[0] == 'W':
                    if self.Clockwise(self.TopS[1],self.MiddleSE[0]):
                        self.TopCC()
                        self.SouthCC()
                    elif self.Opposites(self.TopS[1],self.MiddleSE[0]):
                        self.TopC()
                        self.TopC()
                        self.SouthCC()
                    else:
                        self.TopC()
                        self.SouthCC()
                else:
                    self.SouthCC()

        elif self.MiddleSE[0] == 'W':
                self.Solution += ['piece n 0 p']
                self.Solution += ['move p n n']
                if self.TopE[0] == 'W':
                    if self.Clockwise(self.TopE[1],self.MiddleSE[1]):
                        self.TopCC()
                        self.EastC()
                    elif self.Opposites(self.TopE[1],self.MiddleSE[1]):
                        self.TopC()
                        self.TopC()
                        self.EastC()
                    else:
                        self.TopC()
                        self.EastC()
                elif self.TopS[0] == 'W':
                    if self.Clockwise(self.TopS[1],self.MiddleSE[1]):
                        self.EastC()
                    elif self.Opposites(self.TopS[1],self.MiddleSE[1]):
                        self.TopCC()
                        self.EastC()
                    else:
                        self.TopC()
                        self.TopC()
                        self.EastC()
                elif self.TopW[0] == 'W':
                    if self.Clockwise(self.TopW[1],self.MiddleSE[1]):
                        self.TopC()
                        self.EastC()
                    elif self.Opposites(self.TopW[1],self.MiddleSE[1]):
                        self.EastC()
                    else:
                        self.TopCC()
                        self.EastC()
                elif self.TopN[0] == 'W':
                    if self.Clockwise(self.TopN[1],self.MiddleSE[1]):
                        self.TopC()
                        self.TopC()
                        self.EastC()
                    elif self.Opposites(self.TopN[1],self.MiddleSE[1]):
                        self.TopC()
                        self.EastC()
                    else:
                        self.EastC()
                else:
                    self.EastC()
        else:
            return False
        return True

    def BottomFour(self):
        if self.BottomN[0] == 'W' or self.BottomN[1] == 'W':
            self.Solution += ['move n n n']
            while self.TopN[0] == 'W':
                self.TopC()
            self.Solution += ['piece p n 0']
            self.Solution += ['move n p n']
            self.NorthC()
            self.FirstFour()
        elif self.BottomW[0] == 'W' or self.BottomW[1] == 'W':
            self.Solution += ['move n n p']
            while self.TopW[0] == 'W':
                self.TopC()
            self.Solution += ['piece 0 n n']
            self.Solution += ['move n p p']
            self.WestC()
            self.FirstFour()
        elif self.BottomS[0] == 'W' or self.BottomS[1] == 'W':
            self.Solution += ['move p n p']
            while self.TopS[0] == 'W':
                self.TopC()
            self.Solution += ['piece n n 0']
            self.Solution += ['move p p p']
            self.SouthC()
            self.FirstFour()
        elif self.BottomE[0] == 'W' or self.BottomE[1] == 'W':
            self.Solution += ['move p n n']
            while self.TopE[0] == 'W':
                self.TopC()
            self.Solution += ['piece 0 n p']
            self.Solution += ['move p p n']
            self.EastC()
            self.FirstFour()
        else:
            return False
        return True

    def TopFour(self):
        if self.TopN[1] == 'W':
            self.Solution += ['piece 0 p n']
            self.Solution += ['move n n p']
            self.NorthC()
            self.FirstFour()
        elif self.TopW[1] == 'W':
            self.Solution += ['piece n p 0']
            self.Solution += ['move p n p']
            self.WestC()
            self.FirstFour()
        elif self.TopS[1] == 'W':
            self.Solution += ['piece 0 p p']
            self.Solution += ['move p n n']
            self.SouthC()
            self.FirstFour()
        elif self.TopE[1] == 'W':
            self.Solution += ['piece p p 0']
            self.Solution += ['move n n n']
            self.EastC()
            self.FirstFour()
        

    def WhiteCross(self):
        self.Solution = ['Cross']
        self.Add = True
        while self.TopN[0] != 'W' or self.TopW[0] != 'W' or self.TopE[0] != 'W' or self.TopS[0] != 'W':
            self.Solution += ['Next']
            if len(self.Solution) > 500:
                return False
            if(self.FirstFour() == False):
                if(self.BottomFour() == False):
                    self.TopFour()

        while self.TopN[1] != 'R':
            self.TopC()                                

        if(self.TopW[1] != 'B'):
            self.WestC()
            self.WhiteCross()
        elif(self.TopS[1] != 'O'):
            self.SouthC()
            self.WhiteCross()

    def CornersFirstFour(self):
        if self.BottomNE[1] == 'W':
            self.Solution += ['piece p n p']
            self.Solution += ['move n p n']
            if self.BottomNE[0] == 'G':
                self.Solution += ['piece n p p']
                self.Solution += ['move p n n']
                self.SouthC()
                self.BottomCC()
                self.SouthCC()
            elif self.BottomNE[0] == 'O':
                self.Solution += ['piece n p n']
                self.Solution += ['move p n p']
                self.WestC()
                self.BottomC()
                self.BottomC()
                self.WestCC()
            elif self.BottomNE[0] == 'R':
                self.Solution += ['piece p p p']
                self.Solution += ['move n n n']
                self.BottomC()
                self.EastC()
                self.BottomCC()
                self.EastCC()
            elif self.BottomNE[0] == 'B':
                self.Solution += ['piece p n p']
                self.Solution += ['move n n p']
                self.BottomC()
                self.BottomC()
                self.NorthC()
                self.BottomCC()
                self.NorthCC()
        elif self.BottomNE[2] == 'W':
            self.Solution += ['piece p n p']
            self.Solution += ['move n p n']
            if self.BottomNE[0] == 'G':
                self.Solution += ['piece p p p']
                self.Solution += ['move n n n']
                self.BottomCC()
                self.NorthCC()
                self.BottomC()
                self.NorthC()
            elif self.BottomNE[0] == 'O':
                self.Solution += ['piece n p p']
                self.Solution += ['move p n n']
                self.BottomC()
                self.BottomC()
                self.EastCC()
                self.BottomC()
                self.EastC()
            elif self.BottomNE[0] == 'R':
                self.Solution += ['piece p p n']
                self.Solution += ['move n n p']
                self.WestCC()
                self.BottomC()
                self.WestC()
            elif self.BottomNE[0] == 'B':
                self.Solution += ['piece n p n']
                self.Solution += ['move p n p']
                self.SouthCC()
                self.BottomC()
                self.BottomC()
                self.SouthC()
        elif self.BottomNW[1] == 'W':
            self.Solution += ['piece p n n']
            self.Solution += ['move n p p']
            if self.BottomNW[0] == 'B':
                self.Solution += ['piece n p n']
                self.Solution += ['move p n p']
                self.SouthCC()
                self.BottomC()
                self.SouthC()
            elif self.BottomNW[0] == 'O':
                self.Solution += ['piece n p p']
                self.Solution += ['move p n n']
                self.EastCC()
                self.BottomC()
                self.BottomC()
                self.EastC()
            elif self.BottomNW[0] == 'R':
                self.Solution += ['piece p p n']
                self.Solution += ['move n n p']
                self.BottomCC()
                self.WestCC()
                self.BottomC()
                self.WestC()
            elif self.BottomNW[0] == 'G':
                self.Solution += ['piece p p p']
                self.Solution += ['move n n n']
                self.BottomC()
                self.BottomC()
                self.NorthCC()
                self.BottomCC()
                self.NorthC()
        elif self.BottomNW[2] == 'W':
            self.Solution += ['piece p n n']
            self.Solution += ['move n p p']
            if self.BottomNW[0] == 'B':
                self.BottomC()
                self.NorthC()
                self.BottomCC()
                self.NorthCC()
            elif self.BottomNW[0] == 'O':
                self.Solution += ['piece p p n']
                self.Solution += ['move n n p']
                self.BottomC()
                self.BottomC()
                self.WestC()
                self.BottomCC()
                self.WestCC()
            elif self.BottomNW[0] == 'R':
                self.Solution += ['piece p p p']
                self.Solution += ['move n n n']
                self.EastC()
                self.BottomCC()
                self.EastCC()
            elif self.BottomNW[0] == 'G':
                self.Solution += ['piece n p p']
                self.Solution += ['move p n n']
                self.SouthC()
                self.BottomC()
                self.BottomC()
                self.SouthCC()
        elif self.BottomSW[1] == 'W':
            self.Solution += ['piece n n n']
            self.Solution += ['move p p p']
            if self.BottomSW[0] == 'B':
                self.Solution += ['piece p p n']
                self.Solution += ['move n n p']
                self.NorthC()
                self.BottomCC()
                self.NorthCC()
            elif self.BottomSW[0] == 'R':
                self.Solution += ['piece p p p']
                self.Solution += ['move n n n']
                self.EastC()
                self.BottomC()
                self.BottomC()
                self.EastCC()
            elif self.BottomSW[0] == 'O':
                self.Solution += ['piece n p n']
                self.Solution += ['move p n p']
                self.BottomC()
                self.WestC()
                self.BottomCC()
                self.WestCC()
            elif self.BottomSW[0] == 'G':
                self.Solution += ['piece n p p']
                self.Solution += ['move p n n']
                self.BottomC()
                self.BottomC()
                self.SouthC()
                self.BottomCC()
                self.SouthCC()
        elif self.BottomSW[2] == 'W':
            self.Solution += ['piece n n n']
            self.Solution += ['move p p p']
            if self.BottomSW[0] == 'B':
                self.Solution += ['piece n p n']
                self.Solution += ['move p n p']
                self.BottomCC()
                self.SouthCC()
                self.BottomC()
                self.SouthC()
            elif self.BottomSW[0] == 'R':
                self.Solution += ['piece p p n']
                self.Solution += ['move n n p']
                self.BottomC()
                self.BottomC()
                self.WestCC()
                self.BottomC()
                self.WestC()
            elif self.BottomSW[0] == 'O':
                self.Solution += ['piece n p p']
                self.Solution += ['move p n n']
                self.EastCC()
                self.BottomC()
                self.EastC()
            elif self.BottomSW[0] == 'G':
                self.Solution += ['piece p p p']
                self.Solution += ['move n n n']
                self.NorthCC()
                self.BottomC()
                self.BottomC()
                self.NorthC()
        elif self.BottomSE[1] == 'W':
            self.Solution += ['piece n n p']
            self.Solution += ['move p p n']
            if self.BottomSE[0] == 'G':
                self.Solution += ['piece p p p']
                self.Solution += ['move n n n']
                self.NorthCC()
                self.BottomC()
                self.NorthC()
            elif self.BottomSE[0] == 'R':
                self.Solution += ['piece p p n']
                self.Solution += ['move n n p']
                self.WestCC()
                self.BottomC()
                self.BottomC()
                self.WestC()
            elif self.BottomSE[0] == 'O':
                self.Solution += ['piece n p p']
                self.Solution += ['move p n n']
                self.BottomCC()
                self.EastCC()
                self.BottomC()
                self.EastC()
            elif self.BottomSE[0] == 'B':
                self.Solution += ['piece n p n']
                self.Solution += ['move p n p']
                self.BottomC()
                self.BottomC()
                self.SouthCC()
                self.BottomC()
                self.SouthC()
        elif self.BottomSE[2] == 'W':
            self.Solution += ['piece n n p']
            self.Solution += ['move p p n']
            if self.BottomSE[0] == 'G':
                self.Solution += ['piece n p p']
                self.Solution += ['move p n n']
                self.BottomC()
                self.SouthC()
                self.BottomCC()
                self.SouthCC()
            elif self.BottomSE[0] == 'R':
                self.Solution += ['piece p p p']
                self.Solution += ['move n n n']
                self.BottomC()
                self.BottomC()
                self.EastC()
                self.BottomCC()
                self.EastCC()
            elif self.BottomSE[0] == 'O':
                self.Solution += ['piece n p n']
                self.Solution += ['move p n p']
                self.WestC()
                self.BottomCC()
                self.WestCC()
            elif self.BottomSE[0] == 'B':
                self.Solution += ['piece p p n']
                self.Solution += ['move n n p']
                self.NorthC()
                self.BottomC()
                self.BottomC()
                self.NorthCC()
        else:
            return False
        return True
                
    def BottomCorners(self):
        if self.BottomNE[0] == 'W':
            if self.TopNE[0] == 'W':
                self.BottomC()
            else:
                self.Solution += ['piece p n p']
                self.Solution += ['move n p n']
                self.NorthCC()
                self.BottomC()
                self.BottomC()
                self.NorthC()
        elif self.BottomNW[0] == 'W':
            if self.TopNW[0] == 'W':
                self.BottomC()
            else:
                self.Solution += ['piece p n n']
                self.Solution += ['move n p p']
                self.NorthC()
                self.BottomC()
                self.BottomC()
                self.NorthCC()
        elif self.BottomSE[0] == 'W':
            if self.TopSE[0] == 'W':
                self.BottomC()
            else:
                self.Solution += ['piece n n p']
                self.Solution += ['move p p n']
                self.SouthC()
                self.BottomC()
                self.BottomC()
                self.SouthCC()
        elif self.BottomSW[0] == 'W':
            if self.TopSW[0] == 'W':
                self.BottomC()
            else:
                self.Solution += ['piece n n n']
                self.Solution += ['move p p p']
                self.SouthCC()
                self.BottomC()
                self.BottomC()
                self.SouthC()
        else:
            return False
        return True

    

    def TopCorners(self):
        if self.TopNE[1] == 'W':
            self.Solution += ['piece p p p']
            self.Solution += ['move n n n']
            self.NorthCC()
            self.BottomC()
            self.BottomC()
            self.NorthC()
        elif self.TopNE[2] == 'W':
            self.Solution += ['piece p p p']
            self.Solution += ['move n n n']
            self.EastC()
            self.BottomC()
            self.BottomC()
            self.EastCC()
        elif self.TopNW[1] == 'W':
            self.Solution += ['piece p p n']
            self.Solution += ['move n n p']
            self.NorthC()
            self.BottomC()
            self.BottomC()
            self.NorthCC()
        elif self.TopNW[2] == 'W':
            self.Solution += ['piece p p n']
            self.Solution += ['move n n p']
            self.WestCC()
            self.BottomC()
            self.BottomC()
            self.WestC()
        elif self.TopSE[1] == 'W':
            self.Solution += ['piece n p p']
            self.Solution += ['move p n n']
            self.SouthC()
            self.BottomC()
            self.BottomC()
            self.SouthCC()
        elif self.TopSE[2] == 'W':
            self.Solution += ['piece n p p']
            self.Solution += ['move p n n']
            self.EastCC()
            self.BottomC()
            self.BottomC()
            self.EastC()
        elif self.TopSW[1] == 'W':
            self.Solution += ['piece n p n']
            self.Solution += ['move p n p']
            self.SouthCC()
            self.BottomC()
            self.BottomC()
            self.SouthC()
        elif self.TopSW[2] == 'W':
            self.Solution += ['piece n p n']
            self.Solution += ['move p n p']
            self.WestC()
            self.BottomC()
            self.BottomC()
            self.WestCC()
    
    

    def WhiteCorners(self):
        while self.TopNE[0] != 'W' or self.TopNW[0] != 'W' or self.TopSE[0] != 'W' or self.TopSW[0] != 'W':
            if (self.CornersFirstFour() == False):
                if (self.BottomCorners() == False):
                    self.TopCorners()

        if self.TopNE[1] != 'R':
            self.NorthCC()
            self.BottomC()
            self.BottomC()
            self.NorthC()
            self.WhiteCorners()

        elif self.TopNW[1] != 'R':
            self.NorthC()
            self.BottomC()
            self.BottomC()
            self.NorthCC()
            self.WhiteCorners()

        elif self.TopSE[1] != 'O':
            self.SouthC()
            self.BottomC()
            self.BottomC()
            self.SouthCC()
            self.WhiteCorners()
                    
                


    # algorithm 2

    def StepTwo(self):
        while self.MiddleNE != ('R','G') or self.MiddleNW != ('R','B') or self.MiddleSE != ('O','G') or self.MiddleSW != ('O','B'):
            self.Solution += ['Next']
            if len(self.Solution) > 500:
                return False
            if 'Y' not in self.BottomN:
                if self.BottomN[0] == 'O':
                    if self.BottomN[1] == 'B':
                        self.TwoSouthWest()
                    elif self.BottomN[1] == 'G':
                        self.TwoSouthEast()
                elif self.BottomN[0] == 'G':
                    self.BottomC()
                    if self.BottomW[1] == 'R':
                        self.TwoEastNorth()
                    elif self.BottomW[1] == 'O':
                        self.TwoEastSouth()
                elif self.BottomN[0] == 'R':
                    self.BottomC()
                    self.BottomC()
                    if self.BottomS[1] == 'G':
                        self.TwoNorthEast()
                    elif self.BottomS[1] == 'B':
                        self.TwoNorthWest()
                elif self.BottomN[0] == 'B':
                    self.BottomCC()
                    if self.BottomE[1] == 'R':
                        self.TwoWestNorth()
                    elif self.BottomE[1] == 'O':
                        self.TwoWestSouth()
                        
            elif 'Y' not in self.BottomW:
                if self.BottomW[0] == 'O':
                    self.BottomCC()
                    if self.BottomN[1] == 'B':
                        self.TwoSouthWest()
                    elif self.BottomN[1] == 'G':
                        self.TwoSouthEast()
                elif self.BottomW[0] == 'G':
                    if self.BottomW[1] == 'R':
                        self.TwoEastNorth()
                    elif self.BottomW[1] == 'O':
                        self.TwoEastSouth()
                elif self.BottomW[0] == 'R':
                    self.BottomC()
                    if self.BottomS[1] == 'G':
                        self.TwoNorthEast()
                    elif self.BottomS[1] == 'B':
                        self.TwoNorthWest()
                elif self.BottomW[0] == 'B':
                    self.BottomC()
                    self.BottomC()
                    if self.BottomE[1] == 'R':
                        self.TwoWestNorth()
                    elif self.BottomE[1] == 'O':
                        self.TwoWestSouth()
                    
            elif 'Y' not in self.BottomS:
                if self.BottomS[0] == 'O':
                    self.BottomC()
                    self.BottomC()
                    if self.BottomN[1] == 'B':
                        self.TwoSouthWest()
                    elif self.BottomN[1] == 'G':
                        self.TwoSouthEast()
                elif self.BottomS[0] == 'G':
                    self.BottomCC()
                    if self.BottomW[1] == 'R':
                        self.TwoEastNorth()
                    elif self.BottomW[1] == 'O':
                        self.TwoEastSouth()
                elif self.BottomS[0] == 'R':
                    if self.BottomS[1] == 'G':
                        self.TwoNorthEast()
                    elif self.BottomS[1] == 'B':
                        self.TwoNorthWest()
                elif self.BottomS[0] == 'B':
                    self.BottomC()
                    if self.BottomE[1] == 'R':
                        self.TwoWestNorth()
                    elif self.BottomE[1] == 'O':
                        self.TwoWestSouth()

            elif 'Y' not in self.BottomE:
                if self.BottomE[0] == 'O':
                    self.BottomC()
                    if self.BottomN[1] == 'B':
                        self.TwoSouthWest()
                    elif self.BottomN[1] == 'G':
                        self.TwoSouthEast()
                elif self.BottomE[0] == 'G':
                    self.BottomC()
                    self.BottomC()
                    if self.BottomW[1] == 'R':
                        self.TwoEastNorth()
                    elif self.BottomW[1] == 'O':
                        self.TwoEastSouth()
                elif self.BottomE[0] == 'R':
                    self.BottomCC()
                    if self.BottomS[1] == 'G':
                        self.TwoNorthEast()
                    elif self.BottomS[1] == 'B':
                        self.TwoNorthWest()
                elif self.BottomE[0] == 'B':
                    if self.BottomE[1] == 'R':
                        self.TwoWestNorth()
                    elif self.BottomE[1] == 'O':
                        self.TwoWestSouth()

            elif 'Y' not in self.MiddleNE and self.MiddleNE != ('R','G'):
                self.TwoNorthEast()

            elif 'Y' not in self.MiddleNW and self.MiddleNW != ('R','B'):
                self.TwoNorthWest()

            elif 'Y' not in self.MiddleSE and self.MiddleSE != ('O','G'):
                self.TwoSouthEast()

            elif 'Y' not in self.MiddleSW and self.MiddleSW != ('O','B'):
                self.TwoSouthWest()
                
            

    def TwoEastSouth(self):
        self.Solution += ['piece n 0 p']
        self.Solution += ['piece 0 n n']
        self.Solution += ['move p p n']
        self.Solution += ['move n p p']
        self.Solution += ['move p p n']
        self.EastCC()
        self.BottomC()
        self.EastC()
        self.BottomC()
        self.SouthC()
        self.BottomCC()
        self.SouthCC()

    def TwoSouthEast(self):
        self.Solution += ['piece n 0 p']
        self.Solution += ['piece p n 0']
        self.Solution += ['move p p n']
        self.Solution += ['move n p p']
        self.Solution += ['move p p n']
        self.SouthC()
        self.BottomCC()
        self.SouthCC()
        self.BottomCC()
        self.EastCC()
        self.BottomC()
        self.EastC()

    def TwoWestSouth(self):
         self.Solution += ['piece n 0 n']
         self.Solution += ['piece 0 n p']
         self.Solution += ['move p p p']
         self.Solution += ['move n p n']
         self.Solution += ['move p p p']
         self.WestC()
         self.BottomCC()
         self.WestCC()
         self.BottomCC()
         self.SouthCC()
         self.BottomC()
         self.SouthC()
 
    def TwoSouthWest(self):
         self.Solution += ['piece n 0 n']
         self.Solution += ['piece p n 0']
         self.Solution += ['move p p p']
         self.Solution += ['move n p n']
         self.Solution += ['move p p p']
         self.SouthCC()
         self.BottomC()
         self.SouthC()
         self.BottomC()
         self.WestC()
         self.BottomCC()
         self.WestCC()

    def TwoWestNorth(self):
        self.Solution += ['piece p 0 n']
        self.Solution += ['piece 0 n p']
        self.Solution += ['move n p p']
        self.Solution += ['move p p n']
        self.Solution += ['move n p p']
        self.WestCC()
        self.BottomC()
        self.WestC()
        self.BottomC()
        self.NorthC()
        self.BottomCC()
        self.NorthCC()

    def TwoNorthWest(self):
        self.Solution += ['piece p 0 n']
        self.Solution += ['piece n n 0']
        self.Solution += ['move n p p']
        self.Solution += ['move p p n']
        self.Solution += ['move n p p']
        self.NorthC()
        self.BottomCC()
        self.NorthCC()
        self.BottomCC()
        self.WestCC()
        self.BottomC()
        self.WestC()


    def TwoEastNorth(self):
         self.Solution += ['piece p 0 p']
         self.Solution += ['piece 0 n n']
         self.Solution += ['move n p n']
         self.Solution += ['move p p p']
         self.Solution += ['move n p n']
         self.EastC()
         self.BottomCC()
         self.EastCC()
         self.BottomCC()
         self.NorthCC()
         self.BottomC()
         self.NorthC()
 
    def TwoNorthEast(self):
         self.Solution += ['piece p 0 p']
         self.Solution += ['piece n n 0']
         self.Solution += ['move n p n']
         self.Solution += ['move p p p']
         self.Solution += ['move n p n']
         self.NorthCC()
         self.BottomC()
         self.NorthC()
         self.BottomC()
         self.EastC()
         self.BottomCC()
         self.EastCC()

    # algorithm 3

    def StepThree(self):
        self.Solution += ['Next']
        if len(self.Solution) > 500:
                return False
        num = 0
        LofYellow = []
        if self.BottomN[0] == 'Y':
            num += 1
            LofYellow += 'R'
        if self.BottomE[0] == 'Y':
            num += 1
            LofYellow += 'G'
        if self.BottomS[0] == 'Y':
            num += 1
            LofYellow += 'O'
        if self.BottomW[0] == 'Y':
            num += 1
            LofYellow += 'B'
        if num == 0:
            self.Solution += ['piece p n 0']
            self.Solution += ['piece 0 n p']
            self.Solution += ['piece n n 0']
            self.Solution += ['piece 0 n n']
            self.ThreeSouth()
            self.ThreeWestInverse()
        elif num == 2:
            if self.Opposites(LofYellow[0],LofYellow[1]):
                if LofYellow[0] == 'R':
                    self.Solution += ['piece 0 n p']
                    self.Solution += ['piece 0 n n']
                    self.ThreeWestInverse()
                else:
                    self.Solution += ['piece n n 0']
                    self.Solution += ['piece p n 0']
                    self.ThreeNorthInverse()
            else:
                if LofYellow[0] == 'R':
                    if LofYellow[1] == 'G':
                        self.Solution += ['piece 0 n n']
                        self.Solution += ['piece n n 0']
                        self.ThreeSouth()
                    else:
                        self.Solution += ['piece 0 n p']
                        self.Solution += ['piece n n 0']
                        self.ThreeEast()
                elif LofYellow[0] == 'G':
                    self.Solution += ['piece 0 n n']
                    self.Solution += ['piece p n 0']
                    self.ThreeWest()
                elif LofYellow[0] == 'O':
                    self.Solution += ['piece 0 n p']
                    self.Solution += ['piece p n 0']
                    self.ThreeNorth()               


    def ThreeSouth(self):
        self.Solution += ['move p p n']
        self.SouthC()
        self.BottomC()
        self.WestC()
        self.BottomCC()
        self.WestCC()
        self.SouthCC()

    def ThreeSouthInverse(self):
        self.Solution += ['move p p n']
        self.SouthC()
        self.WestC()
        self.BottomC()
        self.WestCC()
        self.BottomCC()
        self.SouthCC()

    def ThreeEast(self):
        self.Solution += ['move n p n']
        self.EastC()
        self.BottomC()
        self.SouthC()
        self.BottomCC()
        self.SouthCC()
        self.EastCC()

    def ThreeEastInverse(self):
        self.Solution += ['move n p n']
        self.EastC()
        self.SouthC()
        self.BottomC()
        self.SouthCC()
        self.BottomCC()
        self.EastCC()

    def ThreeNorth(self):
        self.Solution += ['move n p p']
        self.NorthC()
        self.BottomC()
        self.EastC()
        self.BottomCC()
        self.EastCC()
        self.NorthCC()

    def ThreeNorthInverse(self):
        self.Solution += ['move n p p']
        self.NorthC()
        self.EastC()
        self.BottomC()
        self.EastCC()
        self.BottomCC()
        self.NorthCC()

    def ThreeWest(self):
        self.Solution += ['move p p p']
        self.WestC()
        self.BottomC()
        self.NorthC()
        self.BottomCC()
        self.NorthCC()
        self.WestCC()

    def ThreeWestInverse(self):
        self.Solution += ['move p p p']
        self.WestC()
        self.NorthC()
        self.BottomC()
        self.NorthCC()
        self.BottomCC()
        self.WestCC()


    # algorithm 4

    def StepFour(self):
        self.Solution += ['Next']
        if len(self.Solution) > 500:
                return False
        num = 0
        LofYellow = []
        if self.BottomNE[0] == 'Y':
            num += 1
            LofYellow += 'T'
        elif self.BottomNE[1] == 'Y':
            LofYellow += 'N'
        else:
            LofYellow += 'E'
            
        if self.BottomSE[0] == 'Y':
            num += 1
            LofYellow += 'T'
        elif self.BottomSE[1] == 'Y':
            LofYellow += 'S'
        else:
            LofYellow += 'E'
            
        if self.BottomSW[0] == 'Y':
            num += 1
            LofYellow += 'T'
        elif self.BottomSW[1] == 'Y':
            LofYellow += 'S'
        else:
            LofYellow += 'W'
            
        if self.BottomNW[0] == 'Y':
            num += 1
            LofYellow += 'T'
        elif self.BottomNW[1] == 'Y':
            LofYellow += 'N'
        else:
            LofYellow += 'W'
            
        if num == 0:
            if LofYellow[0] == 'N' and LofYellow[2] == 'S':
                self.FourWestNorth()
            elif LofYellow[0] == 'E' and LofYellow[2] == 'W':
                self.FourNorthEast()
            elif LofYellow[0] == 'N' and LofYellow[1] == 'E' and LofYellow[2] == 'W':
                self.FourEastSouth()
            elif LofYellow[0] == 'N' and LofYellow[1] == 'S' and LofYellow[2] == 'W':
                self.FourNorthEast()
            elif LofYellow[0] == 'E' and LofYellow[1] == 'S' and LofYellow[2] == 'S':
                self.FourSouthWest()
            elif LofYellow[0] == 'E' and LofYellow[1] == 'E' and LofYellow[2] == 'S':
                self.FourWestNorth()
            self.StepFour()
        elif num == 1:
            if LofYellow[0] == 'T' and LofYellow[1] == 'E':
                self.FourEastSouth()
            elif LofYellow[0] == 'T' and LofYellow[1] == 'S':
                self.FourNorthWest()
            elif LofYellow[1] == 'T' and LofYellow[2] == 'S':
                self.FourSouthWest()
            elif LofYellow[1] == 'T' and LofYellow[2] == 'W':
                self.FourEastNorth()
            elif LofYellow[2] == 'T' and LofYellow[3] == 'W':
                self.FourWestNorth()
            elif LofYellow[2] == 'T' and LofYellow[3] == 'N':
                self.FourSouthEast()
            elif LofYellow[3] == 'T' and LofYellow[0] == 'N':
                self.FourNorthEast()
            elif LofYellow[3] == 'T' and LofYellow[0] == 'E':
                self.FourWestSouth()
        elif num == 2:
            if LofYellow[0] == 'T' and LofYellow[1] == 'T' and LofYellow[2] == 'S':
                self.FourNorthEast()
            elif LofYellow[0] == 'T' and LofYellow[1] == 'E' and LofYellow[2] == 'W':
                self.FourWestNorth()
            elif LofYellow[0] == 'N' and LofYellow[1] == 'S' and LofYellow[2] == 'T':
                self.FourSouthWest()
            elif LofYellow[0] == 'E' and LofYellow[1] == 'T' and LofYellow[2] == 'T':
                self.FourEastSouth()
                
            elif LofYellow[0] == 'T' and LofYellow[1] == 'T' and LofYellow[2] == 'W':
                self.FourSouthWestInverse()
            elif LofYellow[0] == 'N' and LofYellow[1] == 'T' and LofYellow[2] == 'T':
                self.FourWestNorthInverse()
            elif LofYellow[0] == 'E' and LofYellow[1] == 'E' and LofYellow[2] == 'T':
                self.FourNorthEastInverse()
            elif LofYellow[0] == 'T' and LofYellow[1] == 'S' and LofYellow[2] == 'S':
                self.FourEastSouthInverse()

            elif LofYellow[0] == 'T' and LofYellow[1] == 'E' and LofYellow[2] == 'T':
                self.FourNorthEast()
            elif LofYellow[0] == 'E' and LofYellow[1] == 'T' and LofYellow[2] == 'S':
                self.FourEastSouth()
            elif LofYellow[0] == 'T' and LofYellow[1] == 'S' and LofYellow[2] == 'T':
                self.FourSouthWest()
            elif LofYellow[0] == 'N' and LofYellow[1] == 'T' and LofYellow[2] == 'W':
                self.FourWestNorth()
            self.StepFour()
            
                
        

    def FourSouthWest(self):
        self.Solution += ['piece n n n']
        self.Solution += ['piece p n p']
        self.Solution += ['piece p n n']
        self.Solution += ['move p p p']
        self.WestC()
        self.BottomC()
        self.WestCC()
        self.BottomC()
        self.WestC()
        self.BottomC()
        self.BottomC()
        self.WestCC()

    def FourSouthWestInverse(self):
        self.Solution += ['piece n n n']
        self.Solution += ['piece p n p']
        self.Solution += ['piece p n n']
        self.Solution += ['move p p p']
        self.WestC()
        self.BottomC()
        self.BottomC()
        self.WestCC()
        self.BottomCC()
        self.WestC()
        self.BottomCC()
        self.WestCC()

    def FourSouthEast(self):
        self.Solution += ['piece n n p']
        self.Solution += ['piece p n p']
        self.Solution += ['piece p n n']
        self.Solution += ['move p p n']
        self.EastCC()
        self.BottomCC()
        self.EastC()
        self.BottomCC()
        self.EastCC()
        self.BottomC()
        self.BottomC()
        self.EastC()

    def FourEastSouth(self):
        self.Solution += ['piece n n n']
        self.Solution += ['piece n n p']
        self.Solution += ['piece p n n']
        self.Solution += ['move p p n']
        self.SouthC()
        self.BottomC()
        self.SouthCC()
        self.BottomC()
        self.SouthC()
        self.BottomC()
        self.BottomC()
        self.SouthCC()

    def FourEastSouthInverse(self):
        self.Solution += ['piece n n n']
        self.Solution += ['piece n n p']
        self.Solution += ['piece p n n']
        self.Solution += ['move p p n']
        self.SouthC()
        self.BottomC()
        self.BottomC()
        self.SouthCC()
        self.BottomCC()
        self.SouthC()
        self.BottomCC()
        self.SouthCC()

    def FourEastNorth(self):
        self.Solution += ['piece n n n']
        self.Solution += ['piece p n n']
        self.Solution += ['piece p n p']
        self.Solution += ['move n p n']
        self.NorthCC()
        self.BottomCC()
        self.NorthC()
        self.BottomCC()
        self.NorthCC()
        self.BottomC()
        self.BottomC()
        self.NorthC()

    def FourNorthEast(self):
        self.Solution += ['piece n n n']
        self.Solution += ['piece n n p']
        self.Solution += ['piece p n p']
        self.Solution += ['move n p n']
        self.EastC()
        self.BottomC()
        self.EastCC()
        self.BottomC()
        self.EastC()
        self.BottomC()
        self.BottomC()
        self.EastCC()

    def FourNorthEastInverse(self):
        self.Solution += ['piece n n n']
        self.Solution += ['piece n n p']
        self.Solution += ['piece p n p']
        self.Solution += ['move n p n']
        self.EastC()
        self.BottomC()
        self.BottomC()
        self.EastCC()
        self.BottomCC()
        self.EastC()
        self.BottomCC()
        self.EastCC()

    def FourNorthWest(self):
        self.Solution += ['piece n n n']
        self.Solution += ['piece n n p']
        self.Solution += ['piece p n p']
        self.Solution += ['move n p p']
        self.WestCC()
        self.BottomCC()
        self.WestC()
        self.BottomCC()
        self.WestCC()
        self.BottomC()
        self.BottomC()
        self.WestC()

    def FourWestNorth(self):
        self.Solution += ['piece p n n']
        self.Solution += ['piece n n p']
        self.Solution += ['piece p n p']
        self.Solution += ['move n p p']
        self.NorthC()
        self.BottomC()
        self.NorthCC()
        self.BottomC()
        self.NorthC()
        self.BottomC()
        self.BottomC()
        self.NorthCC()

    def FourWestNorthInverse(self):
        self.Solution += ['piece p n n']
        self.Solution += ['piece n n p']
        self.Solution += ['piece p n p']
        self.Solution += ['move n p p']
        self.NorthC()
        self.BottomC()
        self.BottomC()
        self.NorthCC()
        self.BottomCC()
        self.NorthC()
        self.BottomCC()
        self.NorthCC()

    def FourWestSouth(self):
        self.Solution += ['piece n n n']
        self.Solution += ['piece n n p']
        self.Solution += ['piece p n p']
        self.Solution += ['move p p p']
        self.SouthCC()
        self.BottomCC()
        self.SouthC()
        self.BottomCC()
        self.SouthCC()
        self.BottomC()
        self.BottomC()
        self.SouthC()


    # algorithm five

    def StepFive(self):
        self.Solution += ['Next']
        if len(self.Solution) > 500:
                return False
        if self.BottomNE[2] == self.BottomSE[2] and self.BottomNW[2] == self.BottomSW[2]:
            self.Solution.pop()
            return
        elif self.BottomNE[2] == self.BottomSE[2]:
            self.FiveWestNorth()
        elif self.BottomSW[1] == self.BottomSE[1]:
            self.FiveNorthEast()
        elif self.BottomSW[2] == self.BottomNW[2]:
            self.FiveEastSouth()
        elif self.BottomNE[1] == self.BottomNW[1]:
            self.FiveSouthWest()
        else:
            self.FiveSouthWest()
            self.StepFive()
            
            

    def FiveSouthWest(self):
 #       self.Solution += ['5 Orange Righty']
        self.Solution += ['piece n n n']
        self.Solution += ['piece n n p']
        self.Solution += ['piece p n p']
        self.Solution += ['move p p p']
        self.WestCC()
        self.SouthC()
        self.WestCC()
        self.NorthC()
        self.NorthC()
        self.WestC()
        self.SouthCC()
        self.WestCC()
        self.NorthC()
        self.NorthC()
        self.WestC()
        self.WestC()

    def FiveSouthEast(self):
 #       self.Solution += ['5 Orange Lefty']
        self.EastC()
        self.SouthCC()
        self.EastC()
        self.NorthC()
        self.NorthC()
        self.EastCC()
        self.SouthC()
        self.EastC()
        self.NorthC()
        self.NorthC()
        self.EastC()
        self.EastC()

    def FiveWestNorth(self):
 #       self.Solution += ['5 Blue Righty']
        self.Solution += ['piece n n n']
        self.Solution += ['piece n n p']
        self.Solution += ['piece p n p']
        self.Solution += ['move p p p']
        self.NorthCC()
        self.WestC()
        self.NorthCC()
        self.EastC()
        self.EastC()
        self.NorthC()
        self.WestCC()
        self.NorthCC()
        self.EastC()
        self.EastC()
        self.NorthC()
        self.NorthC()

    def FiveWestSouth(self):
 #       self.Solution += ['5 Blue Lefty']
        self.SouthC()
        self.WestCC()
        self.SouthC()
        self.EastC()
        self.EastC()
        self.SouthCC()
        self.WestC()
        self.SouthC()
        self.EastC()
        self.EastC()
        self.SouthC()
        self.SouthC()

    def FiveNorthEast(self):
 #       self.Solution += ['5 Red Righty']
        self.EastCC()
        self.NorthC()
        self.EastCC()
        self.SouthC()
        self.SouthC()
        self.EastC()
        self.NorthCC()
        self.EastCC()
        self.SouthC()
        self.SouthC()
        self.EastC()
        self.EastC()

    def FiveNorthWest(self):
 #       self.Solution += ['5 Red Lefty']
        self.WestC()
        self.NorthCC()
        self.WestC()
        self.SouthC()
        self.SouthC()
        self.WestCC()
        self.NorthC()
        self.WestC()
        self.SouthC()
        self.SouthC()
        self.WestC()
        self.WestC()

    def FiveEastSouth(self):
 #       self.Solution += ['5 Green Righty']
        self.SouthCC()
        self.EastC()
        self.SouthCC()
        self.WestC()
        self.WestC()
        self.SouthC()
        self.EastCC()
        self.SouthCC()
        self.WestC()
        self.WestC()
        self.SouthC()
        self.SouthC()

    def FiveEastNorth(self):
        #self.Solution += ['5 Green Lefty']
        self.NorthC()
        self.EastCC()
        self.NorthC()
        self.WestC()
        self.WestC()
        self.NorthCC()
        self.EastC()
        self.NorthC()
        self.WestC()
        self.WestC()
        self.NorthC()
        self.NorthC()


    # algorithm 6

    def StepSix(self):
        self.Solution += ['Next']
        if len(self.Solution) > 500:
                return False
        if self.BottomN[1] == self.BottomNE[1] and self.BottomS[1] == self.BottomSE[1]:
            self.Solution.pop()
        elif self.BottomN[1] == self.BottomNE[1]:
            if self.BottomS[1] == self.BottomSE[2]:
                self.SixSouthEast()
            else:
                self.SixSouthWest()
        elif self.BottomS[1] == self.BottomSE[1]:
            if self.BottomN[1] == self.BottomNE[2]:
                self.SixNorthEast()
            else:
                self.SixNorthWest()
        elif self.BottomE[1] == self.BottomNE[2]:
            if self.BottomW[1] == self.BottomSW[1]:
                self.SixWestSouth()
            else:
                self.SixWestNorth()
        elif self.BottomW[1] == self.BottomNW[2]:
            if self.BottomE[1] == self.BottomSE[1]:
                self.SixEastSouth()
            else:
                self.SixEastNorth()
        else:
            self.SixEastNorth()
            self.StepSix()
            return

        while self.BottomN[1] != 'R':
            self.BottomC()
            if len(self.Solution) > 500:
                return False
            #self.Solution += ['Yellow Clockwise']
        
        

    def SixSouthWest(self):
        #self.Solution += ['6 Orange Right']
        self.SouthC()
        self.SouthC()
        self.BottomCC()
        self.WestCC()
        self.EastC()
        self.SouthC()
        self.SouthC()
        self.WestC()
        self.EastCC()
        self.BottomCC()
        self.SouthC()
        self.SouthC()

    def SixSouthEast(self):
        #self.Solution += ['6 Orange Left']
        self.SouthC()
        self.SouthC()
        self.BottomC()
        self.WestCC()
        self.EastC()
        self.SouthC()
        self.SouthC()
        self.WestC()
        self.EastCC()
        self.BottomC()
        self.SouthC()
        self.SouthC()

    def SixNorthEast(self):
        #self.Solution += ['6 Red Right']
        self.NorthC()
        self.NorthC()
        self.BottomCC()
        self.WestC()
        self.EastCC()
        self.NorthC()
        self.NorthC()
        self.WestCC()
        self.EastC()
        self.BottomCC()
        self.NorthC()
        self.NorthC()

    def SixNorthWest(self):
        #self.Solution += ['6 Red Left']
        self.NorthC()
        self.NorthC()
        self.BottomC()
        self.WestC()
        self.EastCC()
        self.NorthC()
        self.NorthC()
        self.WestCC()
        self.EastC()
        self.BottomC()
        self.NorthC()
        self.NorthC()

    def SixWestNorth(self):
        #self.Solution += ['6 Blue Right']
        self.WestC()
        self.WestC()
        self.BottomCC()
        self.NorthCC()
        self.SouthC()
        self.WestC()
        self.WestC()
        self.NorthC()
        self.SouthCC()
        self.BottomCC()
        self.WestC()
        self.WestC()

    def SixWestSouth(self):
        #self.Solution += ['6 Blue Left']
        self.WestC()
        self.WestC()
        self.BottomC()
        self.NorthCC()
        self.SouthC()
        self.WestC()
        self.WestC()
        self.NorthC()
        self.SouthCC()
        self.BottomC()
        self.WestC()
        self.WestC()


    def SixEastNorth(self):
        #self.Solution += ['6 Green Left']
        self.EastC()
        self.EastC()
        self.BottomC()
        self.NorthC()
        self.SouthCC()
        self.EastC()
        self.EastC()
        self.NorthCC()
        self.SouthC()
        self.BottomC()
        self.EastC()
        self.EastC()

    def SixEastSouth(self):
        #self.Solution += ['6 Green Right']
        self.EastC()
        self.EastC()
        self.BottomCC()
        self.NorthC()
        self.SouthCC()
        self.EastC()
        self.EastC()
        self.NorthCC()
        self.SouthC()
        self.BottomCC()
        self.EastC()
        self.EastC()

"""
C = cube()
C.MixUp()
C.PrintCube()
for i in range(len(C.MixedSteps)):
    print C.MixedSteps[i]
C.WhiteCross()
C.WhiteCorners()
C.StepTwo()
C.StepThree()
C.StepFour()
C.StepFive()
C.StepSix()
C.PrintCube()
for i in range(len(C.Solution)):
    print C.Solution[i]
"""
