
class GameController:

    def __init__(self, m, v) -> None:
        """Constructs a controller for the freeCell game.

        Keyword arguments:
        m -- model, in this case the Board
        v -- view, in this case the GameView
        """
        self.m = m
        self.v = v

    def moveCardBetweenTabs(self, st, dt) -> None:
        """Moves a card from the tableau to another tableau

        Keyword arguments:
        st -- source tableau
        dt -- destination 
        """
        c = st[0]

        if(self.isValidMoveForTab(c, dt)):
            c = st.pop(0)
            dt.insert(0, c)
            self.updateView()



    def moveCardToFreeCell(self, st, dfcIdx) -> None:
        """Moves a card from the tableau to a freecell.

        Keyword arguments:
        st -- source tableau
        dfcIdx -- destination freecell index
        """
        fc = self.m.getFreeCells()
        c = st[0]

        if(self.isValidMoveForFreeCell(c, dfcIdx)):
            c = st.pop(0)
            fc[dfcIdx] = c
            self.updateView()

    def moveCardFromFreeCell(self, sfcIdx, dt) -> None:
        """Moves a card from a freecell to a tableau

        Keyword arguments:
        sfc -- source free cell index
        dt -- destination tableau
        """
        fc = self.m.getFreeCells()
        c = fc[sfcIdx]

        if(self.isValidMoveForTab(c, dt)):
            fc[sfcIdx] = None
            dt.insert(0, c)
            self.updateView()

    def moveTabtoFoundation(self, t) -> None:
        """Moves a card from a tableau to a foundation pile

        Keyword arguments:
        t -- source tableau
        """
        f = self.m.getFoundations()
        c = t[0]
        s = c.getSuit()

        if(self.isValidMoveForFoundation(c)):
            c = t.pop(0)
            f[s] = c
            self.updateView()

    def moveFreeCelltoFoundation(self, fcIdx) -> None:
        """Moves a card from a freecell to a foundation

        Keyword arguments:
        fc -- source free cell index
        """
        fc = self.m.getFreeCells()
        f = self.m.getFoundations()
        c = fc[fcIdx]
        s = c.getSuit()

        if(self.isValidMoveForFoundation(c)):
            fc[idx] = None
            f[s] = c
            self.updateView()

    def isValidMoveForTab(self, c, dt) -> bool:
        """Checks that card placement is valid.

        Keyword arguments:
        c -- card in question
        dt -- destination tableau
        """
        if c == None:
            return False

        topC = dt[0] #Top Card of Destination Tableau
        s = c.getSuit()

        if((s == 0 or s == 1) and (topC.getSuit() == 2 or topC.getSuit() == 3)):
            if(topC.getNumber() - c.getNumber() == 1):
                return True

        elif((s == 2 or s == 3) and (topC.getSuit() == 0 or topC.getSuit() == 1)):
            if(topC.getNumber() - c.getNumber() == 1):
                return True


        return False
    
    def isValidMoveForFreeCell(self, c, fcIdx) -> bool:
        """Checks that card placement is valid into freecell.

        Keyword arguments:
        c -- card in question
        fc -- destination freecell index
        """

        if c == None:
            return False
        f = self.m.getFreeCells()

        if(f[fcIdx] == None):
            return True

        return False

    
    def isValidMoveForFoundation(self, c) -> bool:
        """Checks that card placement is valid into foundation pile.

        Keyword arguments:
        c -- card in question
        
        """
        if c == None:
            return False

        f = self.m.getFoundations()
        s = c.getSuit()
        v = c.getNumber()

        if(f[s] == None and v == 1):
            return True
        elif(f[s] != None and v - f[s].getNumber() == 1):
            return True
            
        return False

    def updateView(self) -> None:
        """Updates the view the controller is connected to.
        In this case, it is the gameView.
        """
        self.v.updateView(self.m)