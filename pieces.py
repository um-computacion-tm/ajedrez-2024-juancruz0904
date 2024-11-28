class Piece:
    def __init__(self, color):
        self.color = color
        self.symbol = ""

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def __str__(self):
        return self.symbol

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'P' if color == 'WHITE' else 'p'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # Lógica de movimiento del peón
        return True

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'R' if color == 'WHITE' else 'r'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # Lógica de movimiento de la torre
        return True

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'N' if color == 'WHITE' else 'n'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # Lógica de movimiento del caballo
        return True

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'B' if color == 'WHITE' else 'b'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # Lógica de movimiento del alfil
        return True

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'Q' if color == 'WHITE' else 'q'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # Lógica de movimiento de la reina
        return True

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K' if color == 'WHITE' else 'k'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # Lógica de movimiento del rey
        return True