from Board import Board
from View import View
from GameController import GameController
import random

seed = 5555
random.seed(seed)
print("Seed:", seed)
b = Board(4)
v = View()
c = GameController(b,v)
v.updateView(b)

for i in range(100):

    t1 = random.randint(0, 7)
    t2 = random.randint(0, 7)

    c.moveCardBetweenTabs(b.getTableau(t1), b.getTableau(t2))

for i in range(5):

    c.moveCardToFreeCell(b.getTableau(0), i % 4)

for i in range(5):
    for j in range(len(b.getTableaus())):
        c.moveCardFromFreeCell(i % 4, b.getTableau(j))
        c.moveTabtoFoundation(b.getTableau(j))


