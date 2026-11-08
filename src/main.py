from game.game import Game
from game.pieces import Rook, King
game = Game()

game = Game()

rook = game.board.get_piece(7, 0)
knight = game.board.get_piece(7, 1)
bishop = game.board.get_piece(7, 2)
queen = game.board.get_piece(7, 3)
king = game.board.get_piece(7, 4)

print("Rook:", game.get_legal_move(rook))
print("Knight:", game.get_legal_move(knight))
print("Bishop:", game.get_legal_move(bishop))
print("Queen:", game.get_legal_move(queen))
print("King:", game.get_legal_move(king))