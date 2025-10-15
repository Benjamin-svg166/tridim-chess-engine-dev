from engine.piece import Piece

def test_piece_position():
    p = Piece("bishop", "white", 0, 2, 3)
    assert p.get_position() == (0, 2, 3)
    p.set_position(1, 4, 4)
    assert p.get_position() == (1, 4, 4)
