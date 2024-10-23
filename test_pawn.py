import unittest

class Piece:
    def __init__(self, color):
        self.color = color

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'P' if color == 'WHITE' else 'p'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # El peon se mueve una casilla en cualquier dirección
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col) 
        
        if row_diff <= 1 and col_diff <= 1: 
            # Verificar que la casilla de destino esté vacía o tenga una pieza del oponente
            destination_piece = board[to_row][to_col]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False

class TestPawnMovement(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.pawn_white = Pawn('WHITE')
        self.pawn_black = Pawn('BLACK')

    def test_pawn_moves_one_square_any_direction(self):
        # Probar movimiento válido
        self.assertTrue(self.pawn_white.is_valid_move(4, 4, 3, 4, self.board))
        self.assertTrue(self.pawn_white.is_valid_move(4, 4, 3, 5, self.board))

        # Probar movimiento inválido (más de una casilla)
        self.assertFalse(self.pawn_white.is_valid_move(4, 4, 2, 4, self.board))
        self.assertFalse(self.pawn_white.is_valid_move(4, 4, 2, 5, self.board))
        self.assertFalse(self.pawn_white.is_valid_move(4, 4, 2, 6, self.board))

    def test_pawn_cannot_capture_same_color_piece(self):
        # Colocar una pieza blanca en la posición de destino
        self.board[4][3] = Piece('WHITE')
        self.assertFalse(self.pawn_white.is_valid_move(4, 4, 4, 3, self.board))

        # El peon negro debería poder moverse a esta posición
        self.assertTrue(self.pawn_black.is_valid_move(4, 4, 3, 4, self.board))

    def test_pawn_can_capture_opponent_piece(self):
        # Colocar una pieza negra en la posición de destino
        self.board[3][4] = Piece('BLACK')
        self.assertTrue(self.pawn_white.is_valid_move(4, 4, 3, 4, self.board))

        # El peon negro no debería poder moverse a esta posición
        self.assertFalse(self.pawn_black.is_valid_move(4, 4, 5, 4, self.board))

if __name__ == '__main__':
    unittest.main()