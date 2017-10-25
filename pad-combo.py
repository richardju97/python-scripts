# pad-combo.py

class Board:
    def __init__(r, c):
        self.rows = r
        self.columns = c
        self.b = []
        self.createBoard()
    def createBoard():
        for i in range(0, self.rows*self.columns):
            b.append(0)
