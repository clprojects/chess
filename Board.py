class Board:
    def __init__(self):
        self.create_board()
    
    def create_board(self):
        rows, cols = (8, 8)
        arr = []

        for j in range(cols):
            col = []
            for j in range(rows):
                col.append(0)
            arr.append(col)
        
        for row in arr:
            print(row)

b = Board()