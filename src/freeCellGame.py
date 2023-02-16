from Board import Board
from View import View
from GameController import GameController

b = Board(4)
v = View()
c = GameController(b,v)
v.updateView(b)

print(b.getTableau(0)[0].toString())

c.moveCardBetweenTabs(b.getTableau(0), b.getTableau(1))

