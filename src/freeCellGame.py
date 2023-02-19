from Board import Board
from View import View
from gameAgent import gameAgent
from GameController import GameController
import random
from Card import Card

seed = random.randint(0, 9999)
random.seed(seed)
print("Seed:", seed)
b = Board(4)
v = View()
c = GameController(b,v)
v.updateView(b)
a = gameAgent(b, c)

a.solve()


