# Posicion de la TORRE

from pieces import Piece, Rook

class Board:
    def __init__(self):
        self.positions = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)
        self.positions[0][0] = Rook("Black") # Black
        self.positions[0][7] = Rook("Black") # Black
        self.positions[7][7] = Rook("White") # White
        self.positions[7][0] = Rook("White") # White
    
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
    
# Movimiento de la TORRE

class Rook(Piece):
    def _init_(self, color):
        super()._init_(color)
        self.symbol = 'R' if color == 'WHITE' else 'r'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        if from_row != to_row and from_col != to_col:
            return False

        # Movimiento vertical
        if from_row == to_row:
            step = 1 if to_col > from_col else -1
            print('from_col: ', from_col)
            print('to_col: ', to_col)
            for col in range(from_col + step, to_col, step):
                if board[from_row][col] is not None:
                    return False

        # Movimiento horizontal
        if from_col == to_col:
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if board[row][from_col] is not None:
                    return False

        # Verifica si la casilla de destino está vacía o contiene una pieza enemiga  
        return board[to_row][to_col] is None or board[to_row][to_col].color != self.color