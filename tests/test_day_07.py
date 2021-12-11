import pytest 

import aoc.day_07


@pytest.fixture(scope='module')
def puzzle_input():
    return [
        '16,1,2,0,4,2,7,1,2,14',
    ]


@pytest.mark.parametrize(
    'to,answer',
    [
        (2, 37),
        (1, 41),
        (3, 39),
        (10, 71),
    ]
)
def test_part_01_examples(puzzle_input, to, answer):
    assert aoc.day_07.main(puzzle_input)[to] == answer

def test_part_01(puzzle_input):
    assert aoc.day_07.part_01(puzzle_input) == 37


@pytest.mark.parametrize(
    'old,new,answer',
    [
        (16, 5, 66),
        (1, 5, 10),
        (2, 5, 6),
        (0, 5, 15),
        (4, 5, 1),
        (7, 5, 3),
        (14, 5, 45),
    ]
)
def test_culmulative_costs(old, new, answer):
    assert aoc.day_07.culmulative_cost(old, new) == answer


def test_part_02(puzzle_input):
    assert aoc.day_07.part_02(puzzle_input) == 168
