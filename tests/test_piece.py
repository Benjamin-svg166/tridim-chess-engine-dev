from engine.board_manager import BoardManager
from engine.piece_logic_engine import PieceLogicEngine
from engine.piece import Piece

def test_knight_moves():
    board = BoardManager()
    logic = PieceLogicEngine(board)
    knight = Piece("knight", "white", 1, 4, 4)
    board.place_piece(knight, 1, 4, 4)
    moves = logic.get_valid_moves(knight)
    assert any(move[0] != 1 for move in moves), "Knight should move across layers"
