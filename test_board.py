# Verificacion de la posicion y movimiento del REY

import unittest
from ajedres import Board, King # type: ignore

class TestAjedrez(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        # Coloca un rey blanco en (7, 4)
        self.board.board[7][4] = King('WHITE') 
        # Coloca otro rey blanco en (6, 4)
        self.board.board[6][4] = King('WHITE') 

    def test_valid_move(self):
        result = self.board.move_piece(7, 4, 6, 4)  # Movimiento válido del rey
        print(f"Resultado del movimiento válido: {result}")  # Para depuración
        self.assertTrue(result)

    def test_invalid_move(self):
        result = self.board.move_piece(7, 4, 5, 4)  # Movimiento inválido del rey
        print(f"Resultado del movimiento inválido: {result}")  # Para depuración
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

# Verificacion de la posicion y movimiento de la REINA

import unittest
from ajedres import Board, Queen # type: ignore

class TestAjedrez(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        # Coloca un reina blanco en (7, 3)
        self.board.board[7][3] = Queen('WHITE') 
        # Coloca otro reina blanco en (6, 3)
        self.board.board[6][3] = Queen('WHITE') 

    def test_valid_move(self):
        result = self.board.move_piece(7, 3, 6, 3)  # Movimiento válido de la reina
        print(f"Resultado del movimiento válido: {result}")  # Para depuración
        self.assertTrue(result)

    def test_invalid_move(self):
        result = self.board.move_piece(7, 3, 5, 4)  # Movimiento inválido de la reina
        print(f"Resultado del movimiento inválido: {result}")  # Para depuración
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

import unittest
from ajedres import Board, Queen # type: ignore

class TestAjedrez(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        # Coloca un reina blanco en (7, 3)
        self.board.board[7][3] = Queen('WHITE') 
        # Coloca otro reina blanco en (6, 3)
        self.board.board[6][3] = Queen('WHITE') 

    def test_valid_move(self):
        result = self.board.move_piece(7, 3, 6, 2)  # Movimiento válido de la reina
        print(f"Resultado del movimiento válido: {result}")  # Para depuración
        self.assertTrue(result)

    def test_invalid_move(self):
        result = self.board.move_piece(7, 3, 5, 4)  # Movimiento inválido de la reina
        print(f"Resultado del movimiento inválido: {result}")  # Para depuración
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()