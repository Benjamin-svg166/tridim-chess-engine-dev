# engine/special_move_handler.py

class SpecialMoveHandler:
    """
    Handles special moves: castling, en passant, promotion.
    Supports layered and floating variants.
    """

    def __init__(self, board_manager, game_tracker):
        self.board = board_manager
        self.tracker = game_tracker

    def is_castling_possible(self, king, rook):
        # Placeholder logic for layered castling
        if king.has_moved or rook.has_moved:
            return False
        # Add layer-aware path clearance check here
        return True

    def is_en_passant_possible(self, pawn, target_pos):
        # Placeholder for floating en passant logic
        last_move = self.tracker.move_history[-1] if self.tracker.move_history else None
        return False  # To be expanded

    def promote_pawn(self, pawn, new_type="queen"):
        # Replace pawn with new piece
        layer, row, col = pawn.get_position()
        promoted = Piece(new_type, pawn.color, layer, row, col)
        self.board.place_piece(promoted, layer, row, col)
        return promoted
