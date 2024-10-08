# Posicion del REY

from pieces import Piece, King

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

# Movimiento del REY

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K' if color == 'WHITE' else 'k'

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
    

# Posicion de la REINA

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

# Movimiento de la REINA

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


# Posicion del CABALLO

from pieces import Piece, Horse

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

# Movimiento del CABALLO

class Horse(Piece):
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
    

# posicion del ALFIL

from pieces import Piece, Bishop

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


# Posicion del PAWN

from pieces import Piece, Pawn

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

# Movimiento del PEON

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