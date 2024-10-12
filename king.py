# Posicion del REY

import horse
from pieces import King, Piece, pieces

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

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if piece and piece.is_valid_move(from_row, from_col, to_row, to_col, self.board):
            # Realiza el movimiento de la pieza
            self.board[to_row][to_col] = piece
            self.board[from_row][from_col] = None
            
            # Verifica si el rey de ese color está en jaque después del movimiento
            king_position = self.find_king_position(piece.color)
            if self.is_in_check(king_position, piece.color):
                print(f"¡El rey {piece.color} está en jaque!")
            return True
        else:
            print("El movimiento no es válido. Intenta nuevamente.")
            return False

    def find_king_position(self, color):
        # Encuentra la posición del rey del color dado
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and isinstance(piece, King) and piece.color == color:
                    return (row, col)
        return None

    def is_in_check(self, king_position, king_color):
        king_row, king_col = king_position
        opponent_color = 'BLACK' if king_color == 'WHITE' else 'WHITE'
        
        # Revisar las direcciones posibles para encontrar piezas enemigas que puedan atacar al rey
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        # Revisar posibles ataques desde peones, caballos, torres, alfiles, reinas y el rey enemigo
        for direction in directions:
            row_step, col_step = direction
            row, col = king_row + row_step, king_col + col_step
            
            while 0 <= row < 8 and 0 <= col < 8:
                piece = self.board[row][col]
                if piece:
                    if piece.color == opponent_color:
                        if piece.is_valid_move(row, col, king_row, king_col, self.board):
                            print("is_valid_move row:", row, "col:", col, "king_row:", king_row,"king_col:", king_col,"self.board:", self.board)
                            return True
                    break
                row += row_step
                col += col_step
        
        # Verificación específica para movimientos del caballo
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for move in knight_moves:
            row, col = king_row + move[0], king_col + move[1]
            if 0 <= row < 8 and 0 <= col < 8:
                piece = self.board[row][col]
                if piece and piece.color == opponent_color and isinstance(piece, Horse):
                    return True

        return False
   

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
    
    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece and piece.color == self.__turn__ and self.__board__.move_piece(from_row, from_col, to_row, to_col):
            self.change_turn()
        else:
            print("Movimiento inválido o pieza incorrecta. Intenta de nuevo.")

    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        print(self.__board__)  # Esto imprimime el tablero

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

        self.symbol = ""  # Cada subclase asignará su propio símbolo.

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def __str__(self):
        return self.symbol