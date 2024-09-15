import unittest
from ajedres import Board, Horse # type: ignore

class TestAjedrez(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        # Coloca un caballo blanco en (7, 1)
        self.board.board[7][1] = Horse('WHITE') 
        # Coloca otro caballo blanco en (7, 2)
        self.board.board[7][2] = Horse('WHITE') 

    def test_valid_move(self):
        result = self.board.move_piece(7, 1, 5, 0)  # Movimiento válido del caballo
        print(f"Resultado del movimiento válido: {result}")  # Para depuración
        self.assertTrue(result)

    def test_invalid_move(self):
        result = self.board.move_piece(7, 1, 5, 1)  # Movimiento inválido del caballo
        print(f"Resultado del movimiento inválido: {result}")  # Para depuración
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()