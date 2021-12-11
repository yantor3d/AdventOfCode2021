import pytest 

import aoc.day_00 as solve

@pytest.fixture(scope='module')
def puzzle_input():
    return [
    ]


def test_part_01(puzzle_input):
    assert solve.part_01(puzzle_input) is None

def test_part_02(puzzle_input):
    assert solve.part_02(puzzle_input) is None
