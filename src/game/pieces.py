class Piece:
    def __init__(self, color: bool, is_alive=True):
        self.color = color
        self.is_alive = is_alive
    
    def __repr__(self):
        if self.color:
            return self.symbol #White
        else: return self.symbol.lower() #Black

    def get_possible_moves(self,row, column):
        """Возвращает список лучей с координатами ГЕОМЕТРИЧЕСКИ возможных ходов."""
        return []

    def get_attacked_squares(self, row, column):
        # по умолчанию: клетки атаки = все клетки из лучей, сплющенные в один список
        return [square
                for ray in self.get_possible_moves(row, column)
                for square in ray]

class Pawn(Piece):
    symbol = "P"
    def get_possible_moves(self, row, column):
        ray = []

        if self.color:
            ray.append((row - 1, column))
            if row == 6:
                ray.append((row - 2, column))
        else:
            ray.append((row + 1, column))
            if row == 1:
                ray.append((row + 2, column))

        return [ray] # список лучей, у пешки он один

        
    

    def get_attacked_squares(self, row, column):
        moves = []

        if self.color:
            moves.append((row - 1, column +1))
            moves.append((row - 1, column -1))
        else:
            moves.append((row + 1, column +1))
            moves.append((row + 1 , column -1))

        return moves


class Knight(Piece):
    symbol = "N"
    def get_possible_moves(self, row, column):
        offsets = [
            (-2, -1),(-2, 1),(2, -1),(2, 1),
            (1, 2),(1, -2),(-1, 2),(-1, -2)
            ]
        ray = []
        for row_offset, column_offset in offsets:
            new_row = row + row_offset
            new_column = column + column_offset
            ray.append([(new_row, new_column)])
        return ray

class Bishop(Piece):
    symbol = "B"
    def get_possible_moves(self, row, column):
        offsets = [
            (1, 1),(-1, -1),
            (-1, 1),(1, -1)
        ]

        rays = []
        for row_offset, column_offset in offsets:
            ray = [] #луч на каждое направление
            for distance in range(1, 8):
                new_row = row + row_offset * distance
                new_column = column + column_offset * distance
                ray.append((new_row, new_column)) 
            rays.append(ray)
        return rays


class Rook(Piece):
    symbol = "R"
    def get_possible_moves(self, row, column):
        offsets = [
            (-1, 0),(1, 0),
            (0, -1),(0, 1)
        ]

        rays = []

        for row_offset, column_offset in offsets:
            ray = [] #луч с направления
            for distance in range(1, 8):
                new_row = row + row_offset * distance
                new_column = column + column_offset * distance
                ray.append((new_row, new_column))
            rays.append(ray)
        return rays

class Queen(Piece):
    symbol = "Q"
    def get_possible_moves(self, row, column):
        rays = Rook(self.color).get_possible_moves(row, column)
        rays += Bishop(self.color).get_possible_moves(row, column)
        return rays


class King(Piece):
    symbol = "K"
    def get_possible_moves(self, row, column):
        offsets = [
            (1, 0),(0, 1),(-1, 0),(0, -1),
            (-1, -1),(1, 1),(-1, 1),(1, -1)
            ]

        rays = []
        for row_offset, column_offset in offsets:
            new_row = row + row_offset
            new_column = column + column_offset
            rays.append([(new_row, new_column)])
        return rays