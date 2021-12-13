import pytest 

import aoc.day_13 as solve

@pytest.fixture(scope='module')
def puzzle_input():
    return [
        '6,10',
        '0,14',
        '9,10',
        '0,3',
        '10,4',
        '4,11',
        '6,0',
        '6,12',
        '4,1',
        '0,13',
        '10,12',
        '3,4',
        '3,0',
        '8,4',
        '1,10',
        '2,14',
        '8,10',
        '9,0',
        '',
        'fold along y=7',
        'fold along x=5',
    ]


def test_part_01(puzzle_input):
    assert solve.part_01(puzzle_input) == 17

@pytest.mark.skip()
def test_part_02(puzzle_input):
    assert solve.part_02(puzzle_input) is None
