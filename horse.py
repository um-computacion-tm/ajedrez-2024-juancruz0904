from pieces import Horse

class Board:
    def __init__(self):
        self.positions = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)
        self.positions[0][1] = Horse("Black") # Black
        self.positions[0][6] = Horse("Black") # Black
        self.positions[7][1] = Horse("White") # White
        self.positions[7][6] = Horse("White") # White