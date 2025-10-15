def place_piece(self, piece, layer, row, col):
    piece.set_position(layer, row, col)
    self.board[layer][row][col] = piece
