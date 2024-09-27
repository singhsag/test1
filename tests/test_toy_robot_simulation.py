from toyrobot.orientation import Orientation
from toyrobot.position import Position
from toyrobot.toy_robot_simulation import ToyRobotSimulation


def invalid_position():
    return Position(x=-1, y=-1, orientation=None)


def origin_position():
    return Position(x=0, y=0, orientation=Orientation.NORTH)


def five_by_five_table():
    return ToyRobotSimulation(5, 5)


def test_position_with_negative_x_axis_should_be_invalid():
    position_valid = five_by_five_table().is_position_valid(Position(x=-1, y=0, orientation=Orientation.NORTH))
    assert not position_valid


def test_position_with_negative_y_axis_should_be_invalid():
    position_valid = five_by_five_table().is_position_valid(Position(x=0, y=-1, orientation=Orientation.NORTH))
    assert not position_valid


def test_position_with_x_axis_greater_than_table_size_should_be_invalid():
    position_valid = five_by_five_table().is_position_valid(Position(x=5, y=0, orientation=Orientation.NORTH))
    assert not position_valid


def test_far_corner_position_is_valid():
    position_valid = five_by_five_table().is_position_valid(Position(x=4, y=4, orientation=Orientation.NORTH))
    assert position_valid


def test_origin_position_is_valid():
    position_valid = five_by_five_table().is_position_valid(origin_position())
    assert position_valid


def test_middle_position_is_valid():
    position_valid = five_by_five_table().is_position_valid(Position(x=2, y=2, orientation=Orientation.NORTH))
    assert position_valid


def test_placing_robot_at_invalid_position_should_be_ignored():
    simulation = five_by_five_table()
    simulation.place_robot(invalid_position())
    assert simulation.robot is None


def test_placing_robot_with_invalid_position_should_ignore_command():
    simulation = five_by_five_table()
    simulation.place_robot(origin_position())
    assert simulation.robot == origin_position()
    simulation.place_robot(invalid_position())
    assert simulation.robot == origin_position()


def test_should_move_one_unit_north():
    simulation = five_by_five_table()
    simulation.place_robot(origin_position())
    simulation.move_robot()
    assert simulation.robot == Position(x=0, y=1, orientation=Orientation.NORTH)


def test_should_not_move_north_beyond_boundary():
    simulation = five_by_five_table()
    simulation.place_robot(Position(x=0, y=4, orientation=Orientation.NORTH))
    simulation.move_robot()
    assert simulation.robot == Position(x=0, y=4, orientation=Orientation.NORTH)


def test_should_turn_left():
    simulation = five_by_five_table()
    simulation.place_robot(origin_position())
    simulation.turn_robot_left()
    assert simulation.robot == Position(x=0, y=0, orientation=Orientation.WEST)


def test_should_turn_right():
    simulation = five_by_five_table()
    simulation.place_robot(origin_position())
    simulation.turn_robot_right()
    assert simulation.robot == Position(x=0, y=0, orientation=Orientation.EAST)


