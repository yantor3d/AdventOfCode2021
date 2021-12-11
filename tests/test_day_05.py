import pytest 

import aoc.day_05

from aoc.day_05 import LineSegment, Point


@pytest.fixture(scope='module')
def puzzle_input():
    return [
        '0,9 -> 5,9',
        '8,0 -> 0,8',
        '9,4 -> 3,4',
        '2,2 -> 2,1',
        '7,0 -> 7,4',
        '6,4 -> 2,0',
        '0,9 -> 2,9',
        '3,4 -> 1,4',
        '0,0 -> 8,8',
        '5,5 -> 8,2',
    ]


@pytest.mark.parametrize(
    'line_segment,points',
    [
        (
            LineSegment.from_str('1,1 -> 3,3'), 
            {Point(1, 1), Point(2, 2), Point(3, 3)}
        ),
        (
            LineSegment.from_str('9,7 -> 7,9'), 
            {Point(9, 7), Point(8, 8), Point(7, 9)}
        )
    ]
)
def test_points(line_segment,points):
    assert set(line_segment.points()) == points


def test_part_01(puzzle_input):
    assert aoc.day_05.part_01(puzzle_input) == 5


def test_part_02(puzzle_input):
    assert aoc.day_05.part_02(puzzle_input) == 12
