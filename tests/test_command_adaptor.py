import textwrap

from toyrobot.command_adaptor import CommandAdaptor
from toyrobot.toy_robot_simulation import ToyRobotSimulation


def run_and_compare_output(given_input: str, expected_output: str):
    output = ""

    def append_output(message: str):
        nonlocal output
        output += message + "\n"

    command_adaptor = CommandAdaptor(ToyRobotSimulation(), append_output)

    for line in given_input.splitlines():
        command_adaptor.process_command(line)

    assert output == expected_output


def test_should_run_example_a():
    given_input = textwrap.dedent("""
    PLACE 0,0,NORTH
    MOVE
    REPORT
    """)
    expected_output = "0,1,NORTH\n"
    run_and_compare_output(given_input, expected_output)


def test_should_run_example_b():
    given_input = textwrap.dedent("""
    PLACE 0,0,NORTH
    LEFT
    REPORT
    """)
    expected_output = "0,0,WEST\n"
    run_and_compare_output(given_input, expected_output)


def test_should_run_example_c():
    given_input = textwrap.dedent("""
    PLACE 1,2,EAST
    MOVE
    MOVE
    LEFT
    MOVE
    REPORT
    """)
    expected_output = "3,3,NORTH\n"
    run_and_compare_output(given_input, expected_output)
