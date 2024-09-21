from bishop import Board


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):
        return True 

    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        print(self.__board__)

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

if __name__ == "__main__":
    game = Chess()

    while game.is_playing():
        game.show_board()  # Mostrar el tablero antes de cada turno

        try:
            # Obtener las coordenadas de origen
            from_input = input(f"Turno de {game.turn}. Mueve desde (fila columna): ").strip()
            if len(from_input.split()) != 2:
                raise ValueError("Debes ingresar dos valores para la fila y la columna.")
            from_row, from_col = map(int, from_input.split())
            
            # Obtener las coordenadas de destino
            to_input = input("Hasta (fila columna): ").strip()
            if len(to_input.split()) != 2:
                raise ValueError("Debes ingresar dos valores para la fila y la columna.")
            to_row, to_col = map(int, to_input.split())

            # Intentar realizar el movimiento
            game.move(from_row, from_col, to_row, to_col)

        except ValueError as ve:
            print(f"Error: {ve}. Por favor, intenta nuevamente.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")