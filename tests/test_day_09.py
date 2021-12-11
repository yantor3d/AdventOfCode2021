import pytest 

import aoc.day_09 as solve

@pytest.fixture(scope='module')
def puzzle_input():
    return [
        '2199943210',
        '3987894921',
        '9856789892',
        '8767896789',
        '9899965678',
    ]


def test_part_01(puzzle_input):
    assert solve.part_01(puzzle_input) == 15


def test_part_02(puzzle_input):
    assert solve.part_02(puzzle_input) == 1134
