from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "White"

    def is_playing(self):
        return True

    @property
    def turn(self):
        return self.__turn__

    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        # Validar las coordenadas
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            raise ValueError("No hay una pieza en la posición de inicio especificada.")
        
        # Mover la pieza en el tablero
        self.__board__.move_piece(from_row, from_col, to_row, to_col)
        # Cambiar de turno
        self.change_turn()

    def show_board(self):
        print(self.__board__)  # Esto imprime el tablero
    
    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

if __name__ == "__main__":
    game = Chess()
    
    while game.is_playing():
        game.show_board()  # Mostrar el tablero            
        
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
        
        game.move(from_row, from_col, to_row, to_col)