import unittest

class Piece:
    def __init__(self, color):
        self.color = color

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'Q' if color == 'WHITE' else 'q'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # La reina se mueve una casilla en cualquier dirección
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col) 
        
        if row_diff <= 1 and col_diff <= 1: 
            # Verificar que la casilla de destino esté vacía o tenga una pieza del oponente
            destination_piece = board[to_row][to_col]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False

class TestQueenMovement(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.queen_white = Queen('WHITE')
        self.queen_black = Queen('BLACK')

    def test_queen_moves_one_square_any_direction(self):
        # Probar movimiento válido
        self.assertTrue(self.queen_white.is_valid_move(4, 4, 5, 5, self.board))
        self.assertTrue(self.queen_white.is_valid_move(4, 4, 3, 4, self.board))
        self.assertTrue(self.queen_white.is_valid_move(4, 4, 2, 4, self.board))
        self.assertTrue(self.queen_white.is_valid_move(4, 4, 2, 6, self.board))

        # Probar movimiento inválido (más de una casilla)
        self.assertFalse(self.queen_white.is_valid_move(4, 4, 2, 3, self.board))
        self.assertFalse(self.queen_white.is_valid_move(4, 4, 3, 2, self.board))

    def test_queen_cannot_capture_same_color_piece(self):
        # Colocar una pieza blanca en la posición de destino
        self.board[2][5] = Piece('WHITE')
        self.assertFalse(self.queen_white.is_valid_move(4, 4, 2, 5, self.board))

        # La reina negro debería poder moverse a esta posición
        self.assertTrue(self.queen_black.is_valid_move(4, 4, 2, 6, self.board))

    def test_queen_can_capture_opponent_piece(self):
        # Colocar una pieza negra en la posición de destino
        self.board[2][6] = Piece('BLACK')
        self.assertTrue(self.queen_white.is_valid_move(4, 4, 2, 6, self.board))

        # La reina negro no debería poder moverse a esta posición
        self.assertFalse(self.queen_black.is_valid_move(4, 4, 3, 6, self.board))

if __name__ == '__main__':
    unittest.main()