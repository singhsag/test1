from dataclasses import dataclass

from toyrobot.orientation import Orientation


@dataclass
class Position:
    x: int
    y: int
    orientation: Orientation

