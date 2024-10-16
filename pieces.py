# Forma y posicion del REY

class Piece:
    def __init__(self, color):
        self.color = color

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K' if color == 'WHITE' else 'k'

class Board:
    def __init__(self):
        self.positions = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)
        self.positions[0][4] = King("BLACK") # Black
        self.positions[7][4] = King("WHITE") # White

# Forma y posicion de la REINA

class Piece:
    def __init__(self, color):
        self.color = color

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'Q' if color == 'WHITE' else 'q'

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

# Forma y posicion de la TORRE

class Piece:
    def __init__(self, color):
        self.color = color

class Rook(Piece):
    def _init_(self, color):
        super()._init_(color)
        self.symbol = 'R' if color == 'WHITE' else 'r'

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

# Forma y posicion del ALFIL

class Piece:
    def __init__(self, color):
        self.color = color

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'B' if color == 'WHITE' else 'b'

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

# Forma y posicion del CABALLO

class Piece:
    def __init__(self, color):
        self.color = color

class Horse(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'H' if color == 'WHITE' else 'h'

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

# Forma y posicion del PEON

class Piece:
    def __init__(self, color):
        self.color = color

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'P' if color == 'WHITE' else 'p'

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
        for row in self.positions:
            for piece in row:
                if piece is None:
                    board_str += ". "
                else:
                    board_str += str(piece) + " "
            board_str += "\n"
        return board_str