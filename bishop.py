from pieces import Bishop

class Board:
    def __init__(self):
        self.positions = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)
        self.positions[0][2] = Bishop("Black") # Black
        self.positions[0][5] = Bishop("Black") # Black
        self.positions[7][2] = Bishop("White") # White
        self.positions[7][5] = Bishop("White") # White