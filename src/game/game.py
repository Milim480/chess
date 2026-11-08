from .board import Board
from .pieces import Pawn, Rook, Knight, Bishop, Queen, King
class Game:
    def __init__(self):
        self.board = Board()
        self.setup_board()
    def setup_board(self):

        for column in range(8):
            self.board.place_piece(6, column, Pawn(True))
            self.board.place_piece(1, column, Pawn(False))

        for column in range(0, 8, 7):
            self.board.place_piece(7, column, Rook(True))
            self.board.place_piece(0, column, Rook(False))
        
        for column in range(1, 7, 5):
             self.board.place_piece(7, column, Knight(True))
             self.board.place_piece(0, column, Knight(False))

        for column in range(2, 6, 3):
            self.board.place_piece(7, column, Bishop(True))
            self.board.place_piece(0, column, Bishop(False))

        for column in range(3, 4):
            self.board.place_piece(7, column, Queen(True))
            self.board.place_piece(0, column, Queen(False))

        for column in range(4, 5):
            self.board.place_piece(7, column, King(True))
            self.board.place_piece(0, column, King(False))

    def get_coordinate_piece(self, piece) -> tuple:
        for row in range(8):
            for column in range(8):
                piece_on_square = self.board.get_piece(row, column)
                if piece_on_square is piece:
                    coordinate = (row, column)
                    return coordinate

    def get_pseudo_legal_move(self, piece):
        row, column = self.get_coordinate_piece(piece) # tuple
        legal_moves = []

        for ray in piece.get_possible_moves(row, column):
            for r, c in ray:
                if not (0 <= r <= 7 and 0 <= c <= 7):
                    break #отсечение ходов которые геометрически возможны но выходят за рамки доски
                target_piece = self.board.get_piece(r, c) #смотрим что внутри поля
                if target_piece is None:
                    legal_moves.append((r, c)) 
                    continue
                if isinstance(piece, Pawn):
                    break   #пешка просто иначе перезапишет себя вместо другой фигуры
                if target_piece.color != piece.color:
                    legal_moves.append((r, c)) # взятие
                break

        if isinstance(piece, Pawn):
            for r, c in piece.get_attacked_squares(row, column):
                if 0 <= r <= 7 and 0 <= c <= 7:
                    target_piece = self.board.get_piece(r, c)
                    if target_piece is not None and target_piece.color != piece.color:
                        legal_moves.append((r, c))
        return legal_moves

    def get_attacked_squares(self, piece, row, column):
        attacked = []

        if isinstance(piece, Pawn): #поможет потом найти шах
            for r, c in piece.get_attacked_squares(row, column):
                if 0 <= r <= 7 and 0 <= c <= 7:
                    attacked.append((r, c))
            return attacked

        for ray in piece.get_possible_moves(row, column):
            for r, c in ray:
                if not (0 <= r <= 7 and 0 <= c <= 7):
                    break                           
                attacked.append((r, c))              
                if self.board.get_piece(r, c) is not None:
                    break                            
        return attacked
    
    def find_king(self, color):
        for row in range(8):
            for column in range(8):
                piece = self.board.get_piece(row, column)
                if isinstance(piece, King) and piece.color == color:
                    return (row, column)
        return None

    def is_in_check(self, color):
        king_position = self.find_king(color)
        if king_position is None:
            return False
        for row in range(8):
            for column in range(8):
                piece = self.board.get_piece(row, column)
                if piece is not None and piece.color != color:
                    if king_position in self.get_attacked_squares(piece, row, column):
                        return True
        return False

    def get_legal_move(self, piece):
        row, column = self.get_coordinate_piece(piece)
        legal_moves = []

        for r, c in self.get_pseudo_legal_move(piece):
            captured = self.board.get_piece(r, c)      # запоминаем, что стояло на клетке
            self.board.place_piece(r, c, piece)        # делаем ход
            self.board.place_piece(row, column, None)

            if not self.is_in_check(piece.color):      # наш король в безопасности?
                legal_moves.append((r, c))

            self.board.place_piece(row, column, piece) # откатываем ход
            self.board.place_piece(r, c, captured)

        return legal_moves