import pytest 

import aoc.day_03

@pytest.fixture(scope='module')
def puzzle_input():
    return [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]


def test_part_01(puzzle_input):
    assert aoc.day_03.part_01(puzzle_input) == 198


def test_part_02(puzzle_input):
    assert aoc.day_03.part_02(puzzle_input) == 230
