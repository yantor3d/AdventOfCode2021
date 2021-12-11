import pytest 

import aoc.day_06


@pytest.fixture(scope='module')
def puzzle_input():
    return [
        '3,4,3,1,2',
    ]


@pytest.mark.parametrize(
    'num_days,answer',
    [
        (3, 7),
        (18, 26),
        (80, 5934),
    ]
)
def test_part_01(puzzle_input, num_days, answer):
    assert aoc.day_06.main(puzzle_input, num_days) == answer


def test_part_02(puzzle_input):
    assert aoc.day_06.part_02(puzzle_input) == 26984457539
