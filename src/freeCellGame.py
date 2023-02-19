from Board import Board
from View import View
from gameAgent import gameAgent
from GameController import GameController
import random
from Card import Card

seed = 5555
random.seed(seed)
print("Seed:", seed)
b = Board(4)
b.setFoundations([Card(0, 13), Card(1, 13), Card(2, 13), Card(3, 12)])
#set up the tableaus so there is only one card left
b.setTableaus([[] for x in range(8)])
b.tableaus[0].append(Card(3, 13))
v = View()
c = GameController(b,v)
v.updateView(b)
a = gameAgent(b, c)

a.solve()


#for i in range(100):

    #t1 = random.randint(0, 7)
    #t2 = random.randint(0, 7)

    #c.moveCardBetweenTabs(b.getTableau(t1), b.getTableau(t2))

#for i in range(5):

    #c.moveCardToFreeCell(b.getTableau(0), i % 4)

#for i in range(5):
    #for j in range(len(b.getTableaus())):
        #c.moveCardFromFreeCell(i % 4, b.getTableau(j))
        #c.moveTabtoFoundation(b.getTableau(j))


