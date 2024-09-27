from toyrobot.orientation import Orientation


def test_should_turn_right_from_north_to_east():
    assert Orientation.NORTH.right() == Orientation.EAST


def test_should_turn_left_from_north_to_west():
    assert Orientation.NORTH.left() == Orientation.WEST


def test_should_turn_right_from_west_to_north():
    assert Orientation.WEST.right() == Orientation.NORTH


def test_should_turn_left_from_west_to_south():
    assert Orientation.WEST.left() == Orientation.SOUTH
