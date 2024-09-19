import unittest
from ajedres import Board, Pawn # type: ignore

class TestAjedrez(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        # Coloca un peón blanco en (6, 0)
        self.board.board[6][0] = Pawn('WHITE') 
        # Coloca otro peón blanco en (5, 0)
        self.board.board[5][0] = Pawn('WHITE') 

    def test_valid_move(self):
        result = self.board.move_piece(6, 0, 5, 0)  # Movimiento válido de un peón
        print(f"Resultado del movimiento válido: {result}")  # Para depuración
        self.assertTrue(result)

    def test_invalid_move(self):
        result = self.board.move_piece(6, 0, 5, 1)  # Movimiento inválido de un peón
        print(f"Resultado del movimiento inválido: {result}")  # Para depuración
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()