from engine.piece import Piece
from engine.board_manager import BoardManager
from engine.move_executor import MoveExecutor

def test_knight_move_execution():
    board = BoardManager()
    knight = Piece("knight", "white", 1, 4, 4)
    board.place_piece(knight, 1, 4, 4)
    executor = MoveExecutor(board)
    success = executor.execute_move(knight, 2, 5, 5)
    assert success, "Knight should be able to move to (2, 5, 5)"
