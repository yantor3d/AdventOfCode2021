import pytest 

import aoc.day_12 as solve

example_a = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end',
]

example_b = [
    'dc-end',
    'HN-start',
    'start-kj',
    'dc-start',
    'dc-HN',
    'LN-dc',
    'HN-end',
    'kj-sa',
    'kj-HN',
    'kj-dc',
]

example_c = [
    'fs-end',
    'he-DX',
    'fs-he',
    'start-DX',
    'pj-DX',
    'end-zg',
    'zg-sl',
    'zg-pj',
    'pj-he',
    'RW-he',
    'fs-DX',
    'pj-RW',
    'zg-RW',
    'start-pj',
    'he-WI',
    'zg-he',
    'pj-fs',
    'start-RW',    
]

@pytest.mark.parametrize(
    'puzzle_input,answer',
    (
        (example_a, 10),
        (example_b, 19),
        (example_c, 226),
    ),
    ids=['A', 'B', 'C']
)
def test_part_01(puzzle_input, answer):
    assert solve.part_01(puzzle_input) == answer


@pytest.mark.parametrize(
    'puzzle_input,answer',
    (
        (example_a, 36),
        (example_b, 103),
        (example_c, 3509),
    ),
    ids=['A', 'B', 'C']
)
def test_part_02(puzzle_input, answer):
    assert solve.part_02(puzzle_input) == answer
