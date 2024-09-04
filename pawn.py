# Posicion del PAWN

from pieces import Pawn, Piece

class Board:
    def __init__(self):
        self.positions = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)
        self.positions[1][0] = Pawn("Black") # Black
        self.positions[1][1] = Pawn("Black") # Black
        self.positions[1][2] = Pawn("Black") # Black
        self.positions[1][3] = Pawn("Black") # Black
        self.positions[1][4] = Pawn("Black") # Black
        self.positions[1][5] = Pawn("Black") # Black
        self.positions[1][6] = Pawn("Black") # Black
        self.positions[1][7] = Pawn("Black") # Black
        self.positions[6][0] = Pawn("White") # White
        self.positions[6][1] = Pawn("White") # White
        self.positions[6][2] = Pawn("White") # White
        self.positions[6][3] = Pawn("White") # White
        self.positions[6][4] = Pawn("White") # White
        self.positions[6][5] = Pawn("White") # White
        self.positions[6][6] = Pawn("White") # White
        self.positions[6][7] = Pawn("White") # White

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
    
# Movimiento del PAWN

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'P' if color == 'WHITE' else 'p'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        direction = -1 if self.color == 'WHITE' else 1
        start_row = 6 if self.color == 'WHITE' else 1

        # Movimiento hacia adelante sin captura
        if from_col == to_col:
            # Movimiento de 1 casilla
            if to_row == from_row + direction and board[to_row][to_col] is None:
                return True
            # Movimiento de 2 casillas desde la posición inicial
            if from_row == start_row and to_row == from_row + 2 * direction and board[from_row + direction][from_col] is None and board[to_row][to_col] is None:
                return True
        
        # Captura diagonal del tablero
        if abs(from_col - to_col) == 1 and to_row == from_row + direction:
            if board[to_row][to_col] is not None and board[to_row][to_col].color != self.color:                
                return True

        return False