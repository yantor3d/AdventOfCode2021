import pytest 

import aoc.day_17 as solve

@pytest.fixture(scope='module')
def puzzle_input():
    return [
        'target area: x=20..30, y=-10..-5',
    ]

def test_part_01(puzzle_input):
    assert solve.part_01(puzzle_input) == 45

def test_part_02(puzzle_input):
    assert solve.part_02(puzzle_input) == 112
