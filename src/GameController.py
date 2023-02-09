
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
        dt -- destination tebleau
        """
        pass

    def moveCard(self, st, dfc) -> None:
        """Moves a card from the tableau to a freecell.

        Keyword arguments:
        st -- source tableau
        dfc -- destination freecell
        """
        pass

    def moveCard(self, sfc, dt) -> None:
        """Moves a card from a freecell to a tableau

        Keyword arguments:
        sfc -- source free cell
        dt -- destination tableau
        """
        pass

    def moveFoundation(self, t) -> None:
        """Moves a card from a tableau to a foundation pile

        Keyword arguments:
        t -- source tableau
        """
        pass

    def moveFoundation(fc) -> None:
        """Moves a card from a freecell to a foundation

        Keyword arguments:
        fc -- source free cell
        """
        pass

    def isValidMove(self, c, dt) -> bool:
        """Checks that card placement is valid.

        Keyword arguments:
        c -- card in question
        dt -- destination tableau
        """
        return False
    
    def isValidMove(self, c, fc) -> bool:
        """Checks that card placement is valid.

        Keyword arguments:
        c -- card in question
        fc -- destination freecell
        """
        return False

    
    def isValidMove(self, c, dfp) -> bool:
        """Checks that card placement is valid

        Keyword arguments:
        c -- card in question
        dfp -- destination foundation pile
        """
        return False

    def updateView(self) -> None:
        """Updates the view the controller is connected to.
        In this case, it is the gameView.
        """
        pass