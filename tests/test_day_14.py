import collections
import pytest 

import aoc.day_14 as solve

@pytest.fixture(scope='module')
def puzzle_input():
    return [
        'NNCB',
        '',
        'CH -> B',
        'HH -> N',
        'CB -> H',
        'NH -> C',
        'HB -> C',
        'HC -> B',
        'HN -> C',
        'NN -> C',
        'BH -> H',
        'NC -> B',
        'NB -> B',
        'BN -> B',
        'BB -> N',
        'BC -> B',
        'CC -> N',
        'CN -> C',
    ]


def data_to_dict(data):
    result = collections.Counter()

    for i, _ in enumerate(data[:-1]):
        key = data[i] + data[i + 1]
        result[key] += 1
    
    return result


def test_part_01_example(puzzle_input):
    data, rules = solve.parse(puzzle_input)
    assert data == data_to_dict('NNCB')

    data = solve.solve(data, rules)
    assert data == data_to_dict('NCNBCHB')

    data = solve.solve(data, rules)
    assert data == data_to_dict('NBCCNBBBCBHCB')

    data = solve.solve(data, rules)
    assert data == data_to_dict('NBBBCNCCNBBNBNBBCHBHHBCHB')

    data = solve.solve(data, rules)
    assert data == data_to_dict('NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')


def test_part_01(puzzle_input):
    assert solve.part_01(puzzle_input) == 1588


def test_part_02(puzzle_input):
    assert solve.part_02(puzzle_input) == 2188189693529
