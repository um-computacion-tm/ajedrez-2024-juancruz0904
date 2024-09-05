# Posicion de la QUEEN

from pieces import Piece, Queen

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
    
# Movimiento de la QUEEN

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'Q' if color == 'WHITE' else 'q'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # La reina se mueve como una torre o un alfil
        if from_row == to_row or from_col == to_col:
            # Movimiento rectilíneo (como una torre)
            # Verificar que no haya piezas en el camino
            step_row = 0 if from_row == to_row else (1 if to_row > from_row else -1)
            step_col = 0 if from_col == to_col else (1 if to_col > from_col else -1)
            for i in range(1, max(abs(to_row - from_row), abs(to_col - from_col))):
                if board[from_row + i * step_row][from_col + i * step_col] is not None:
                    return False
            # El movimiento es válido si la casilla de destino está vacía o contiene una pieza del oponente
            destination_piece = board[to_row][to_col]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        elif abs(to_row - from_row) == abs(to_col - from_col):
            # Movimiento diagonal (como un alfil)
            step_row = 1 if to_row > from_row else -1
            step_col = 1 if to_col > from_col else -1
            for i in range(1, abs(to_row - from_row)):
                if board[from_row + i * step_row][from_col + i * step_col] is not None:
                    return False
            destination_piece = board[to_row][to_col]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False