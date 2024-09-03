# posicion del ALFIL

from pieces import Bishop, Piece

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

# Movimiento del ALFIL

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'B' if color == 'WHITE' else 'b'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # El alfil se mueve en diagonal, por lo que la diferencia entre filas y columnas debe ser igual
        if abs(to_row - from_row) == abs(to_col - from_col):
            # Verificar que no haya piezas en el camino
            step_row = 1 if to_row > from_row else -1
            step_col = 1 if to_col > from_col else -1
            for i in range(1, abs(to_row - from_row)):
                if board[from_row + i * step_row][from_col + i * step_col] is not None:
                    return False
            # El movimiento es válido si la casilla de destino está vacía o contiene una pieza del oponente
            destination_piece = board[to_row][to_col]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False