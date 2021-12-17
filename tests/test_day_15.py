import pytest 

import aoc.day_15 as solve

@pytest.fixture(scope='module')
def puzzle_input():
    return [
        '1163751742',
        '1381373672',
        '2136511328',
        '3694931569',
        '7463417111',
        '1319128137',
        '1359912421',
        '3125421639',
        '1293138521',
        '2311944581',
    ]


def test_part_01(puzzle_input):
    assert solve.part_01(puzzle_input) == 40

def test_part_02(puzzle_input):
    assert solve.part_02(puzzle_input) == 315
