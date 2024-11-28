class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        # Colocamos los peones en su posición inicial
        for i in range(8):
            self.board[1][i] = Pawn('BLACK')
            self.board[6][i] = Pawn('WHITE')
        # Colocamos las torres en su posición inicial
        self.board[0][0] = self.board[0][7] = Rook('BLACK')
        self.board[7][0] = self.board[7][7] = Rook('WHITE')
        # Colocamos los caballos en su posición inicial
        self.board[0][1] = self.board[0][6] = Knight('BLACK')
        self.board[7][1] = self.board[7][6] = Knight('WHITE')
        # Colocamos los alfiles en su posición inicial
        self.board[0][2] = self.board[0][5] = Bishop('BLACK')
        self.board[7][2] = self.board[7][5] = Bishop('WHITE')
        # Colocamos las reinas en su posición inicial
        self.board[0][3] = Queen('BLACK')
        self.board[7][3] = Queen('WHITE')
        # Colocamos los reyes en su posición inicial
        self.board[0][4] = King('BLACK')
        self.board[7][4] = King('WHITE')

    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += " ".join([str(piece) if piece else '.' for piece in row]) + "\n"
        return board_str

    def get_piece(self, row, col):
        return self.board[row][col]

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if piece and piece.is_valid_move(from_row, from_col, to_row, to_col):
            self.board[to_row][to_col] = piece
            self.board[from_row][from_col] = None
            return True
        else:
            print('El movimiento no es valido, intente nuevamente')
            return False

class Piece:
    def __init__(self, color):
        self.color = color
        self.symbol = ""

    def is_valid_move(self, from_row, from_col, to_row, to_col):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def __str__(self):
        return self.symbol

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'R' if color == 'WHITE' else 'r'        

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

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K' if color == 'WHITE' else 'k'

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
                if piece and piece.color == opponent_color and isinstance(piece, Knight):
                    return True

        return False