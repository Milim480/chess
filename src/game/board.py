class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
    def __repr__(self):
        column_label = ["a", "b", "c", "d", "e", "f", "g", "h"]
        cells = []
        for row in self.board:
            cells.append([])
            for piece in row:
                if piece == None:
                    cells[-1].append(".")
                else: cells[-1].append(repr(piece))
        rows = []
        for row in cells:
            rows.append(" ".join(row))

        numbered_rows = []
        for index, row in enumerate(rows):
            numbered_rows.append(f"{8 - index}  {row}")  

        numbered_rows.append("   " + " ".join(column_label))

        return "\n".join(numbered_rows)


    def get_piece(self, row, column) -> Piece | None:
        piece = self.board[row][column]
        return piece


    def place_piece(self, row, column, piece):
        self.board[row][column] = piece


    def move_piece(self, from_row, from_column, to_row, to_column):
        piece = self.get_piece(from_row, from_column)
        self.place_piece(to_row, to_column, piece)
        self.place_piece(from_row, from_column, None)
    