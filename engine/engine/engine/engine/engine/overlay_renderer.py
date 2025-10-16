# engine/overlay_renderer.py

class OverlayRenderer:
    """
    Visualizes threats, control zones, and piece dynamics.
    Supports immersive overlays for training and AI hints.
    """

    def __init__(self, board_manager, logic_engine):
        self.board = board_manager
        self.logic = logic_engine

    def render_overlay(self, piece):
        """
        Returns a list of highlighted positions for the given piece.
        Used for UI overlays or immersive training.
        """
        valid_moves = self.logic.get_valid_moves(piece)
        highlights = []

        for move in valid_moves:
            layer, row, col = move
            highlights.append({
                "layer": layer,
                "row": row,
                "col": col,
                "type": "valid_move"
            })

        return highlights
