import unittest

class Piece:
    def __init__(self, color):
        self.color = color

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K' if color == 'WHITE' else 'k'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # El rey se mueve una casilla en cualquier dirección
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col) 
        
        if row_diff <= 1 and col_diff <= 1: 
            # Verificar que la casilla de destino esté vacía o tenga una pieza del oponente
            destination_piece = board[to_row][to_col]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False

class TestKingMovement(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.king_white = King('WHITE')
        self.king_black = King('BLACK')

    def test_king_moves_one_square_any_direction(self):
        # Probar movimiento válido
        self.assertTrue(self.king_white.is_valid_move(4, 4, 5, 5, self.board))
        self.assertTrue(self.king_white.is_valid_move(4, 4, 3, 3, self.board))
        self.assertTrue(self.king_white.is_valid_move(4, 4, 5, 3, self.board))
        self.assertTrue(self.king_white.is_valid_move(4, 4, 4, 3, self.board))

        # Probar movimiento inválido (más de una casilla)
        self.assertFalse(self.king_white.is_valid_move(4, 4, 6, 6, self.board))
        self.assertFalse(self.king_white.is_valid_move(4, 4, 2, 2, self.board))
        self.assertFalse(self.king_white.is_valid_move(4, 4, 4, 2, self.board))

    def test_king_cannot_capture_same_color_piece(self):
        # Colocar una pieza blanca en la posición de destino
        self.board[5][5] = Piece('WHITE')
        self.assertFalse(self.king_white.is_valid_move(4, 4, 5, 5, self.board))

        # El rey negro debería poder moverse a esta posición
        self.assertTrue(self.king_black.is_valid_move(4, 4, 5, 5, self.board))

    def test_king_can_capture_opponent_piece(self):
        # Colocar una pieza negra en la posición de destino
        self.board[5][5] = Piece('BLACK')
        self.assertTrue(self.king_white.is_valid_move(4, 4, 5, 5, self.board))

        # El rey negro no debería poder moverse a esta posición
        self.assertFalse(self.king_black.is_valid_move(4, 4, 5, 5, self.board))

if __name__ == '__main__':
    unittest.main()