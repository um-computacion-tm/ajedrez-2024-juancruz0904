import unittest
from ajedres import Board, Rook # type: ignore

class TestAjedrez(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        # Coloca un torre blanco en (7, 0)
        self.board.board[7][0] = Rook('WHITE') 
        # Coloca otro torre blanco en (7, 1)
        self.board.board[7][1] = Rook('WHITE') 

    def test_valid_move(self):
        result = self.board.move_piece(7, 0, 5, 0)  # Movimiento válido de la torre
        print(f"Resultado del movimiento válido: {result}")  # Para depuración
        self.assertTrue(result)

    def test_invalid_move(self):
        result = self.board.move_piece(7, 0, 6, 1)  # Movimiento inválido de la torre
        print(f"Resultado del movimiento inválido: {result}")  # Para depuración
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()