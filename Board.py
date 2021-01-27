

class Board:
    def __init__(self):
        self.create_board()
    
    def create_board(self):
        #Change rows and cols to 17 if using replica chess board
        """
        rows, cols = (8, 8)
        """
        arr = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

        """
        for i in range(cols):
            col = []
            for j in range(rows):
                col.append(0)
            arr.append(col)
        """

        #Code below is to create a somewhat replica chess board, may need to be modified if actually used
        """
        for i in range(cols):
            col = []
            for j in range(rows):
                if (j % 2) == 0:
                    col.append('|')
                else:
                    if (i % 2) == 0:
                        col.append('-')
                    else:
                        col.append(0)
            arr.append(col)
        """

        for row in arr:
            print(*row)

class Piece:

    killed = False
    white = False

    def __init__(self, piecetype, white):
        self.piecetype = piecetype
        self.white = white

class Pawn(Piece):

    count = 0

    def __init__(self, white):
        self.white = white
        piecetype = "pawn"
        super().__init__(piecetype, white)

class Bishop(Piece):
    def __init__(self, white):
        self.white = white
        piecetype = "bishop"
        super().__init__(piecetype, white)

class Knight(Piece):
    def __init__(self, white):
        self.white = white
        piecetype = "knight"
        super().__init__(piecetype, white)

class Rook(Piece):
    def __init__(self, white):
        self.white = white
        piecetype = "rook"
        super().__init__(piecetype, white)

class Queen(Piece):
    def __init__(self, white):
        self .hite = white
        piecetype = "queen"
        super().__init__(piecetype, white)

class King(Piece):

    count = 0
    
    def __init__(self, white):
        self.white = white
        piecetype = "queen"
        super().__init__(piecetype, white)
        
a = Pawn(True)
b = Bishop(True)
c = Knight(True)
d = Rook(True)
e = Queen(True)
f = King(True)

print(a.white, a.piecetype, a.killed)
"""
print(b white, b.piecetype, b.killed)
print(c white, c.piecetype, c.killed)
print(d white, d.piecetype, d.killed)
print(e white, e.piecetype, e.killed)
print(f white, f.piecetype, f.killed, f.count)
"""

b = Board()