# engine/game_state_tracker.py

class GameStateTracker:
    """
    Tracks turn order, move history, active player, and game state.
    Supports alternate lines, undo, and layered cognition.
    """

    def __init__(self):
        self.turn = "white"
        self.move_history = []
        self.board_snapshots = []

    def switch_turn(self):
        self.turn = "black" if self.turn == "white" else "white"

    def record_move(self, piece, from_pos, to_pos):
        move = {
            "piece": repr(piece),
            "from": from_pos,
            "to": to_pos,
            "turn": self.turn
        }
        self.move_history.append(move)
        self.board_snapshots.append(self._snapshot_board())
        self.switch_turn()

    def _snapshot_board(self):
        # Placeholder for deep copy of board state
        return "snapshot"

    def undo_last_move(self):
        if self.move_history:
            self.move_history.pop()
            self.board_snapshots.pop()
            self.switch_turn()
