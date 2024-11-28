import unittest

class Piece:
    def __init__(self, color):
        self.color = color

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'N' if color == 'WHITE' else 'n'

    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # El caballo se mueve una casilla en cualquier dirección
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col) 
        
        if row_diff <= 1 and col_diff <= 1: 
            # Verificar que la casilla de destino esté vacía o tenga una pieza del oponente
            destination_piece = board[to_row][to_col]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False

class TestKnightMovement(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.Knight_white = Knight('WHITE')
        self.Knight_black = Knight('BLACK')

    def test_knight_moves_one_square_any_direction(self):
        # Probar movimiento válido
        self.assertTrue(self.Knight_white.is_valid_move(0, 1, 2, 0, self.board))
        self.assertTrue(self.Knight_white.is_valid_move(0, 1, 2, 2, self.board))

        # Probar movimiento inválido (más de una casilla)
        self.assertFalse(self.Knight_white.is_valid_move(0, 1, 1, 1, self.board))
        self.assertFalse(self.Knight_white.is_valid_move(0, 1, 0, 2, self.board))

    def test_knight_cannot_capture_same_color_piece(self):
        # Colocar una pieza blanca en la posición de destino
        self.board[3][3] = Piece('WHITE')
        self.assertFalse(self.Knight_white.is_valid_move(4, 4, 3, 3, self.board))

        # El caballo negro debería poder moverse a esta posición
        self.assertTrue(self.Knight_black.is_valid_move(4, 4, 2, 3, self.board))

    def test_knight_can_capture_opponent_piece(self):
        # Colocar una pieza negra en la posición de destino
        self.board[2][3] = Piece('BLACK')
        self.assertTrue(self.Knight_white.is_valid_move(4, 4, 2, 3, self.board))

        # El caballo negro no debería poder moverse a esta posición
        self.assertFalse(self.Knight_black.is_valid_move(4, 4, 2, 6, self.board))

if __name__ == '__main__':
    unittest.main()