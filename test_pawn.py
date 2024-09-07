import unittest
from ajedres import Board, Pawn

class TestAjedrez(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        # Coloca un peón blanco en (1, 0)
        self.board.board[1][0] = Pawn('WHITE') 
        # Coloca otro peón blanco en (3, 0)
        self.board.board[3][0] = Pawn('WHITE') 

    def test_valid_move(self):
        result = self.board.move_piece(1, 0, 3, 0)  # Movimiento válido de un peón
        print(f"Resultado del movimiento válido: {result}")  # Para depuración
        self.assertTrue(result)

    def test_invalid_move(self):
        result = self.board.move_piece(1, 0, 2, 2)  # Movimiento inválido de un peón
        print(f"Resultado del movimiento inválido: {result}")  # Para depuración
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()