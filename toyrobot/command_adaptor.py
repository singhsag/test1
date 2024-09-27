import re

from typing import Callable

from toyrobot.toy_robot_simulation import ToyRobotSimulation
from toyrobot.orientation import Orientation

from toyrobot.position import Position


class CommandAdaptor:

    def __init__(self, toy_robot_simulation: ToyRobotSimulation, logger: Callable[[str], None]):
        self.toy_robot_simulation = toy_robot_simulation
        self.logger = logger

    def process_command(self, command_string: str):
        cmd = command_string.split(" ")[0]

        if cmd == "PLACE":
            self.place(command_string)
        elif cmd == "MOVE":
            self.toy_robot_simulation.move_robot()
        elif cmd == "LEFT":
            self.toy_robot_simulation.turn_robot_left()
        elif cmd == "RIGHT":
            self.toy_robot_simulation.turn_robot_right()
        elif cmd == "REPORT":
            self.report()

    def place(self, command_string):
        match = re.match(r"PLACE (\d+),(\d+),(NORTH|EAST|SOUTH|WEST)", command_string)
        if match is not None:
            self.toy_robot_simulation.place_robot(Position(
                x=int(match.group(1)),
                y=int(match.group(2)),
                orientation=Orientation[match.group(3)]))

    def report(self):
        robot_pos = self.toy_robot_simulation.robot
        if robot_pos is not None:
            self.logger(f'{robot_pos.x},{robot_pos.y},{robot_pos.orientation.name}')
