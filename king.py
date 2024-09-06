# Posicion del REY

from pieces import King, Piece

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

# Forma del tablero

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
    
# Movimiento del REY

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K' if color == 'WHITE' else 'k'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # El rey se mueve una casilla en cualquier dirección
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        
        if row_diff <= 1 and col_diff <= 1:
            # Verificar que la casilla de destino esté vacía o tenga una pieza del oponente
            destination_piece = board[to_row][to_col]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False