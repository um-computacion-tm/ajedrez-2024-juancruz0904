from pieces import Rook

class Board:
    def __init__(self):
        self.positions = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)
        self.positions[0][0] = Rook("Black") # Black
        self.positions[0][7] = Rook("Black") # Black
        self.positions[7][7] = Rook("White") # White
        self.positions[7][0] = Rook("White") # White
        
    def get_piece(self, row, col):
        return self.__positions__[row][col]