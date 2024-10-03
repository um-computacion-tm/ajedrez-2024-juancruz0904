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

# Verificacion de la posicion y movimiento de la TORRE

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

# Verificacion de la posicion y movimiento del ALFIL

import unittest
from ajedres import Board, Bishop # type: ignore

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

# Verificacion de la posicion y movimiento del CABALLO

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

# Verificacion de la posicion y movimiento del PEON

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