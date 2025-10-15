# engine/piece.py

class Piece:
    """
    Represents a chess piece in tridimensional space.
    Stores type, color, position, and movement metadata.
    """

    def __init__(self, piece_type, color, layer, row, col):
        self.piece_type = piece_type.lower()  # e.g., 'knight', 'rook'
        self.color = color.lower()            # 'white' or 'black'
        self.layer = layer
        self.row = row
        self.col = col
        self.has_moved = False                # Useful for castling, en passant

    def get_position(self):
        return (self.layer, self.row, self.col)

    def set_position(self, layer, row, col):
        self.layer = layer
        self.row = row
        self.col = col

    def __repr__(self):
        return f"{self.color.capitalize()} {self.piece_type.capitalize()} at ({self.layer}, {self.row}, {self.col})"
