import unittest

from board import Board

class Pawn:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "P" if self.color == 'WHITE' else "p"

class Rook:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "R" if self.color == 'WHITE' else "r"

class Knight:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "N" if self.color == 'WHITE' else "n"

class Bishop:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "B" if self.color == 'WHITE' else "b"

class Queen:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "Q" if self.color == 'WHITE' else "q"

class King:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "K" if self.color == 'WHITE' else "k"

class TestBoardSetup(unittest.TestCase):

    def test_initial_setup(self):
        board = Board()

        # Verificar peones
        for i in range(8):
            self.assertIsInstance(board.get_piece(1, i), Pawn)
            self.assertEqual(board.get_piece(1, i).color, 'BLACK')
            self.assertIsInstance(board.get_piece(6, i), Pawn)
            self.assertEqual(board.get_piece(6, i).color, 'WHITE')

        # Verificar torres
        self.assertIsInstance(board.get_piece(0, 0), Rook)
        self.assertEqual(board.get_piece(0, 0).color, 'BLACK')
        self.assertIsInstance(board.get_piece(0, 7), Rook)
        self.assertEqual(board.get_piece(0, 7).color, 'BLACK')
        self.assertIsInstance(board.get_piece(7, 0), Rook)
        self.assertEqual(board.get_piece(7, 0).color, 'WHITE')
        self.assertIsInstance(board.get_piece(7, 7), Rook)
        self.assertEqual(board.get_piece(7, 7).color, 'WHITE')

        # Verificar caballos
        self.assertIsInstance(board.get_piece(0, 1), Knight)
        self.assertEqual(board.get_piece(0, 1).color, 'BLACK')
        self.assertIsInstance(board.get_piece(0, 6), Knight)
        self.assertEqual(board.get_piece(0, 6).color, 'BLACK')
        self.assertIsInstance(board.get_piece(7, 1), Knight)
        self.assertEqual(board.get_piece(7, 1).color, 'WHITE')
        self.assertIsInstance(board.get_piece(7, 6), Knight)
        self.assertEqual(board.get_piece(7, 6).color, 'WHITE')

        # Verificar alfiles
        self.assertIsInstance(board.get_piece(0, 2), Bishop)
        self.assertEqual(board.get_piece(0, 2).color, 'BLACK')
        self.assertIsInstance(board.get_piece(0, 5), Bishop)
        self.assertEqual(board.get_piece(0, 5).color, 'BLACK')
        self.assertIsInstance(board.get_piece(7, 2), Bishop)
        self.assertEqual(board.get_piece(7, 2).color, 'WHITE')
        self.assertIsInstance(board.get_piece(7, 5), Bishop)
        self.assertEqual(board.get_piece(7, 5).color, 'WHITE')

        # Verificar reinas
        self.assertIsInstance(board.get_piece(0, 3), Queen)
        self.assertEqual(board.get_piece(0, 3).color, 'BLACK')
        self.assertIsInstance(board.get_piece(7, 3), Queen)
        self.assertEqual(board.get_piece(7, 3).color, 'WHITE')

        # Verificar reyes
        self.assertIsInstance(board.get_piece(0, 4), King)
        self.assertEqual(board.get_piece(0, 4).color, 'BLACK')
        self.assertIsInstance(board.get_piece(7, 4), King)
        self.assertEqual(board.get_piece(7, 4).color, 'WHITE')

if __name__ == '__main__':
    unittest.main()