import unittest
from unittest.mock import patch, MagicMock

class Chess:
    def is_playing(self):
        return True

    def show_board(self):
        pass

    def move(self, from_row, from_col, to_row, to_col):
        pass

class TestChessGame(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        '0 0',  # from_input
        '1 0'   # to_input
    ])
    @patch.object(Chess, 'is_playing', side_effect=[True, False])
    def test_chess_main_loop(self, mock_is_playing, mock_input):
        # Crear una instancia de Chess usando un mock para métodos dependientes
        game = Chess()

        with patch.object(game, 'show_board') as mock_show_board:
            with patch.object(game, 'move') as mock_move:
                from __main__ import main  # Importa la función principal desde el módulo principal
                main()  # Ejecuta la función principal

                # Verificar que los métodos se llamaron correctamente
                mock_show_board.assert_called_once()
                mock_move.assert_called_once_with(0, 0, 1, 0)

if __name__ == "__main__":
    unittest.main()