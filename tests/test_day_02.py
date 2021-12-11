import pytest 

import aoc.day_02

@pytest.fixture(scope='module')
def puzzle_input():
    return [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]


def test_part_01(puzzle_input):
    assert aoc.day_02.part_01(puzzle_input) == 150


def test_part_02(puzzle_input):
    assert aoc.day_02.part_02(puzzle_input) == 900
