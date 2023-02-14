
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
        c = st.peek()

        if(self.isValidMove(c, dt)):
            c = st.pop
            dt.push(c)
            self.updateView()



    def moveCard(self, st, fcIdx) -> None:
        """Moves a card from the tableau to a freecell.

        Keyword arguments:
        st -- source tableau
        dfcIdx -- destination freecell index
        """
        fc = self.m.getFreeCells()
        c = st.peek()

        if(self.isValidMove(c, dfcIdx)):
            c = st.pop()
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
            dt.push(c)
            self.updateView()

    def moveFoundation(self, t) -> None:
        """Moves a card from a tableau to a foundation pile

        Keyword arguments:
        t -- source tableau
        """
        f = self.m.getFoundations()
        c = t.peek()
        s = c.getSuit()

        if(self.isValidMove(c, f[s])):
            c = t.pop()
            f[s] = c
            self.updateView()

    def moveFoundation(fcIdx) -> None:
        """Moves a card from a freecell to a foundation

        Keyword arguments:
        fc -- source free cell index
        """
        fc = self.m.getFreeCells()
        f = self.m.getFoundations()

        c = fc[fcIdx]
        s = c.getSuit()

        if(self.isValidMove(c, f[s])):
            fc[idx] =  None
            f = c
            self.updateView()

    def isValidMove(self, c, dt) -> bool:
        """Checks that card placement is valid.

        Keyword arguments:
        c -- card in question
        dt -- destination tableau
        """
        return False
    
    def isValidMove(self, c, fcIdx) -> bool:
        """Checks that card placement is valid.

        Keyword arguments:
        c -- card in question
        fc -- destination freecell index
        """
        f = self.m.getFreeCells()

        if(f[fcIdx] == None):
            return True

        return False

    
    def isValidMove(self, c) -> bool:
        """Checks that card placement is valid

        Keyword arguments:
        c -- card in question
        
        """
        if(f[fcIdx] == None):
            return True

        return False

    def updateView(self) -> None:
        """Updates the view the controller is connected to.
        In this case, it is the gameView.
        """
        self.v.updateView(m)