from pieces import Pawn

class Board:
    def __init__(self):
        self.positions = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)
        self.positions[1][0] = Pawn("Black") # Black
        self.positions[1][1] = Pawn("Black") # Black
        self.positions[1][2] = Pawn("Black") # Black
        self.positions[1][3] = Pawn("Black") # Black
        self.positions[1][4] = Pawn("Black") # Black
        self.positions[1][5] = Pawn("Black") # Black
        self.positions[1][6] = Pawn("Black") # Black
        self.positions[1][7] = Pawn("Black") # Black
        self.positions[6][0] = Pawn("White") # White
        self.positions[6][1] = Pawn("White") # White
        self.positions[6][2] = Pawn("White") # White
        self.positions[6][3] = Pawn("White") # White
        self.positions[6][4] = Pawn("White") # White
        self.positions[6][5] = Pawn("White") # White
        self.positions[6][6] = Pawn("White") # White
        self.positions[6][7] = Pawn("White") # White