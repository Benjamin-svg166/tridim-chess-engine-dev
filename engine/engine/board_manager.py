# engine/board_manager.py

class BoardManager:
    """
    Handles creation and manipulation of 3D boards.
    Supports floating boards, layer transitions, and piece placement.
    """

    def __init__(self, layers=3, rows=8, cols=8):
        self.layers = layers
        self.rows = rows
        self.cols = cols
        self.board = self._initialize_board()

    def _initialize_board(self):
        """
        Initializes a 3D board as a list of layers,
        each containing an 8x8 grid initialized with None.
        """
        return [[[None for _ in range(self.cols)] for _ in range(self.rows)] for _ in range(self.layers)]

    def place_piece(self, piece, layer, row, col):
        """
        Places a piece at the specified 3D coordinate.
        """
        self.board[layer][row][col] = piece

    def remove_piece(self, layer, row, col):
        """
        Removes a piece from the specified 3D coordinate.
        """
        self.board[layer][row][col] = None

    def get_piece(self, layer, row, col):
        """
        Returns the piece at the specified 3D coordinate.
        """
        return self.board[layer][row][col]

    def is_valid_position(self, layer, row, col):
        """
        Checks if the given position is within board bounds.
        """
        return 0 <= layer < self.layers and 0 <= row < self.rows and 0 <= col < self.cols
