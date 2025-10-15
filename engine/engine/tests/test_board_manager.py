from engine.board_manager import BoardManager

def test_board_initialization():
    bm = BoardManager()
    assert bm.get_piece(0, 0, 0) is None
    assert bm.is_valid_position(2, 7, 7) is True
    assert bm.is_valid_position(3, 0, 0) is False
