# engine/position_evaluator.py

class PositionEvaluator:
    """
    Evaluates board positions based on material, mobility,
    and layered control. Supports AI overlays and drill grading.
    """

    def __init__(self, board_manager):
        self.board = board_manager

    def evaluate(self):
        score = 0
        for layer in range(len(self.board.board)):
            for row in range(len(self.board.board[layer])):
                for col in range(len(self.board.board[layer][row])):
                    piece = self.board.board[layer][row][col]
                    if piece:
                        score += self._piece_value(piece)
        return score

    def _piece_value(self, piece):
        values = {
            "pawn": 1,
            "knight": 3,
            "bishop": 3,
            "rook": 5,
            "queen": 9,
            "king": 0  # King is invaluable
        }
        base = values.get(piece.piece_type, 0)
        return base if piece.color == "white" else -base
