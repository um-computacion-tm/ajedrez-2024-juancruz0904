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

    # forma del tablero

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str
        
    def get_piece(self, row, col):
        return self.__positions__[row][col]