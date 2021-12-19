import pytest 

import aoc
import aoc.day_19 as solve

@pytest.fixture(scope='module')
def puzzle_input():
    return aoc.puzzle_input('day_19', 'test_data')


def test_part_01(puzzle_input):
    assert solve.part_01(puzzle_input) is None

def test_part_02(puzzle_input):
    assert solve.part_02(puzzle_input) is None
