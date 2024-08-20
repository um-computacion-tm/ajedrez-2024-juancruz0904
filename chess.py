class Chess:
    def __init__(self):
        self.__board__ = board()
        self.__turn__ = "White"

    def move(
        self,
        from_row,
        from_col,
        to_row
        to_col,
    ):
        # validate coords
        piece = self.board.get_piece(from_row, from_col)
        self.change_turn()

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"