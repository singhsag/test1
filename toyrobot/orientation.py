from enum import Enum


class Orientation(bytes, Enum):
    NORTH = (0, 0, 1)
    EAST = (1, 1, 0)
    SOUTH = (2, 0, -1)
    WEST = (3, -1, 0)

    def __new__(cls, value, forward_x, forward_y):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.forward_x = forward_x
        obj.forward_y = forward_y
        return obj

    def left(self):
        ordinal = self._value_ - 1
        if ordinal < 0:
            ordinal = len(Orientation) - 1
        return Orientation(ordinal)

    def right(self):
        ordinal = self._value_ + 1
        if ordinal >= len(Orientation):
            ordinal = 0
        return Orientation(ordinal)

