from engine.piece_logic_engine import PieceLogicEngine
from engine.game_state_tracker import GameStateTracker
from engine.board_manager import BoardManager

class MoveExecutor:
    """
    Executes validated moves, updates board state,
    and records game history.
    """

    def __init__(self, board_manager):
        self.board = board_manager
        self.logic = PieceLogicEngine(board_manager)
        self.tracker = GameStateTracker()

    def execute_move(self, piece, target_layer, target_row, target_col):
        valid_moves = self.logic.get_valid_moves(piece)
        target = (target_layer, target_row, target_col)

        if target not in valid_moves:
            return False  # Invalid move

        from_pos = piece.get_position()
        self.board.remove_piece(*from_pos)
        self.board.place_piece(piece, *target)
        self.tracker.record_move(piece, from_pos, target)
        return True
