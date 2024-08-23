from pieces import King

class Board:
    def __init__(self):
        self.positions = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)
        self.positions[0][4] = King("Black") # Black
        self.positions[7][4] = King("White") # White