import unittest

class Piece:
    def __init__(self, color):
        self.color = color

class Horse(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'H' if color == 'WHITE' else 'h'

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

class TestHorseMovement(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.Horse_white = Horse('WHITE')
        self.Horse_black = Horse('BLACK')

    def test_horse_moves_one_square_any_direction(self):
        # Probar movimiento válido
        self.assertTrue(self.Horse_white.is_valid_move(0, 1, 2, 0, self.board))
        self.assertTrue(self.Horse_white.is_valid_move(0, 1, 2, 2, self.board))

        # Probar movimiento inválido (más de una casilla)
        self.assertFalse(self.Horse_white.is_valid_move(0, 1, 1, 1, self.board))
        self.assertFalse(self.Horse_white.is_valid_move(0, 1, 0, 2, self.board))

    def test_horse_cannot_capture_same_color_piece(self):
        # Colocar una pieza blanca en la posición de destino
        self.board[4][5] = Piece('WHITE')
        self.assertFalse(self.Horse_white.is_valid_move(4, 5, 3, 3, self.board))

        # El caballo negro debería poder moverse a esta posición
        self.assertTrue(self.Horse_black.is_valid_move(4, 5, 3, 3, self.board))

    def test_horse_can_capture_opponent_piece(self):
        # Colocar una pieza negra en la posición de destino
        self.board[4][5] = Piece('BLACK')
        self.assertTrue(self.Horse_white.is_valid_move(4, 5, 2, 5, self.board))

        # El caballo negro no debería poder moverse a esta posición
        self.assertFalse(self.Horse_black.is_valid_move(4, 5, 2, 5, self.board))

if __name__ == '__main__':
    unittest.main()