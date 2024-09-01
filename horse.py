# Posicion del HORSE

from pieces import Horse, Piece

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
    
# Movimiento del HORSE

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'H' if color == 'WHITE' else 'h'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # El caballo se mueve en forma de "L"
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            # El movimiento es válido si la casilla de destino está vacía o contiene una pieza del oponente
            destination_piece = board[to_row][to_col]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False