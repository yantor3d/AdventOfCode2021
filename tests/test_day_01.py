import os
import pytest

import aoc.day_01


@pytest.fixture(scope='module')
def puzzle_input():
    return [
        '199',
        '200',
        '208',
        '210',
        '200',
        '207',
        '240',
        '269',
        '260',
        '263',
    ]


def test_part_01(puzzle_input):
    assert aoc.day_01.part_01(puzzle_input) == 7


def test_part_02(puzzle_input):
    assert aoc.day_01.part_02(puzzle_input) == 5