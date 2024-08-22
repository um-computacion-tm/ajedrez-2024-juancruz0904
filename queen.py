from pieces import Queen

class Board:
    def __init__(self):
        self.positions = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)
        self.positions[0][3] = Queen("Black") # Black
        self.positions[7][3] = Queen("White") # White