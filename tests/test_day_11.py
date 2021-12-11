import pytest 

import aoc.day_11 as solve

@pytest.fixture(scope='module')
def puzzle_input():
    return [
        '5483143223',
        '2745854711',
        '5264556173',
        '6141336146',
        '6357385478',
        '4167524645',
        '2176841721',
        '6882881134',
        '4846848554',
        '5283751526',
    ]


def test_part_01(puzzle_input):
    assert solve.part_01(puzzle_input) == 1656

def test_part_02(puzzle_input):
    assert solve.part_02(puzzle_input) == 195
