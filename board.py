class Board:
    def __init__(self):
        # Inicializamos un tablero de 8x8 con None en todas las posiciones
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

# Posiciones de las piesas

    def setup_board(self):
        # Colocamos los peones en su posición inicial
        for i in range(8):
            self.board[1][i] = Pawn('BLACK')
            self.board[6][i] = Pawn('WHITE')

        # Colocamos las torres en su posición inicial
        self.board[0][0] = self.board[0][7] = Rook('BLACK')
        self.board[7][0] = self.board[7][7] = Rook('WHITE')

        # Colocamos los caballos en su posición inicial
        self.board[0][1] = self.board[0][6] = Horse('BLACK')
        self.board[7][1] = self.board[7][6] = Horse('WHITE')

        # Colocamos los alfiles en su posición inicial
        self.board[0][2] = self.board[0][5] = Bishop('BLACK')
        self.board[7][2] = self.board[7][5] = Bishop('WHITE')

        # Colocamos las reinas en su posición inicial
        self.board[0][3] = Queen('BLACK')
        self.board[7][3] = Queen('WHITE')

        # Colocamos los reyes en su posición inicial
        self.board[0][4] = King('BLACK')
        self.board[7][4] = King('WHITE')

# Construye el tablero

    def __str__(self):
        board_str = ""
        for row in self.board:
            for piece in row:
                if piece is None:
                    board_str += ". "
                else:
                    board_str += str(piece) + " "
            board_str += "\n"
        return board_str   
        
    def get_piece(self, row, col):
        # Devuelve la pieza en la posición dada
        return self.board[row][col]