
class GameController:

    def __init__(self, m, v) -> None:
        """Constructs a controller for the freeCell game.

        Keyword arguments:
        m -- model, in this case the Board
        v -- view, in this case the GameView
        """
        self.m = m
        self.v = v

    def moveCard(self, st, dt) -> None:
        """Moves a card from the tableau to another tableau

        Keyword arguments:
        st -- source tableau
        dt -- destination 
        """
        c = st.index(0)

        if(self.isValidMove(c, dt)):
            c = st.pop(0)
            dt.append(0, c)
            self.updateView()



    def moveCard(self, st, dfcIdx) -> None:
        """Moves a card from the tableau to a freecell.

        Keyword arguments:
        st -- source tableau
        dfcIdx -- destination freecell index
        """
        fc = self.m.getFreeCells()
        c = st.index(0)

        if(self.isValidMove(c, dfcIdx)):
            c = st.pop(0)
            fc[dfcIdx] = c
            self.updateView()

    def moveCard(self, sfcIdx, dt) -> None:
        """Moves a card from a freecell to a tableau

        Keyword arguments:
        sfc -- source free cell index
        dt -- destination tableau
        """
        fc = self.m.getFreeCells()
        c = fc[sfcIdx]

        if(self.isValidMove(c, dt)):
            fc[sfcIdx] = None
            dt.append(0, c)
            self.updateView()

    def moveFoundation(self, t) -> None:
        """Moves a card from a tableau to a foundation pile

        Keyword arguments:
        t -- source tableau
        """
        c = t.index(0)

        if(self.isValidMove(c)):
            c = t.pop(0)
            f[s] = c
            self.updateView()

    def moveFoundation(self, fcIdx) -> None:
        """Moves a card from a freecell to a foundation

        Keyword arguments:
        fc -- source free cell index
        """
        fc = self.m.getFreeCells()
        c = fc[fcIdx]

        if(self.isValidMove(c)):
            fc[idx] =  None
            f = c
            self.updateView()

    def isValidMove(self, c, dt) -> bool:
        """Checks that card placement is valid.

        Keyword arguments:
        c -- card in question
        dt -- destination tableau
        """

        topC = dt.index(0) #Top Card of Destination Tableau
        s = c.getSuit()

        if((s == 0 or s == 1) and (topC.getSuit() == 2 or topC.getSuit() == 3)):
            if(topC.getValue() - c.getValue <= 1):
                return True

        elif((s == 2 or s == 3) and (topC.getSuit() == 0 or topC.getSuit() == 1)):
            if(topC.getValue() - c.getValue <= 1):
                return True


        return False
    
    def isValidMove(self, c, fcIdx) -> bool:
        """Checks that card placement is valid into freecell.

        Keyword arguments:
        c -- card in question
        fc -- destination freecell index
        """
        f = self.m.getFreeCells()

        if(f[fcIdx] == None):
            return True

        return False

    
    def isValidMove(self, c) -> bool:
        """Checks that card placement is valid into foundation pile.

        Keyword arguments:
        c -- card in question
        
        """
        f = self.m.getFoundations()
        s = c.getSuit()
        v = c.getValue()

        if(f[s] == None and v == 1):
            return True
        elif(f[s] != None and v - f[s].getValue <= 1):
            return True
            
        return False

    def updateView(self) -> None:
        """Updates the view the controller is connected to.
        In this case, it is the gameView.
        """
        self.v.updateView(m)