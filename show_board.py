from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):
        return True

    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece and piece.color == self.__turn__ and self.__board__.move_piece(from_row, from_col, to_row, to_col):
            self.change_turn()
        else:
            print("Movimiento inválido o pieza incorrecta. Intenta de nuevo.")

    def turn(self):
        return self.__turn__

    def show_board(self):
        print(self.__board__)  # Esto imprime el tablero

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

if __name__ == "__main__":
    game = Chess()
    
    while game.is_playing():
        print("Turno del jugador:", game.turn())  # Mostrar el jugador actual
        game.show_board()  # Mostrar el tablero

        # Simular un movimiento o pedir al usuario que ingrese un movimiento
        from_row, from_col, to_row, to_col = 1, 0, 2, 0  # Por ejemplo, un movimiento
        game.move(from_row, from_col, to_row, to_col)