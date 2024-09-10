import unittest
from ajedres import Board, Bishop

class TestAjedrez(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        # Coloca un alfil blanco en (7, 2)
        self.board.board[7][2] = Bishop('WHITE') 
        # Coloca otro alfil blanco en (6, 2)
        self.board.board[6][2] = Bishop('WHITE') 

    def test_valid_move(self):
        result = self.board.move_piece(7, 2, 6, 3)  # Movimiento válido del alfil
        print(f"Resultado del movimiento válido: {result}")  # Para depuración
        self.assertTrue(result)

    def test_invalid_move(self):
        result = self.board.move_piece(7, 2, 7, 3)  # Movimiento inválido del alfil
        print(f"Resultado del movimiento inválido: {result}")  # Para depuración
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()