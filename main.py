import sys

from toyrobot.toy_robot_simulation import ToyRobotSimulation
from toyrobot.command_adaptor import CommandAdaptor

if __name__ == "__main__":
    command_adaptor = CommandAdaptor(ToyRobotSimulation(), print)
    print("Toy Robot Simulator is now ready for commands!")
    for line in sys.stdin:
        command_adaptor.process_command(line.rstrip())
