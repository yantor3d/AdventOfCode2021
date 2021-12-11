import collections
import copy
import itertools
import time

import aoc

DIGITS = {
    'abcefg':  0,
    'cf':      1,
    'acdeg':   2,
    'acdefg':  3,
    'bcdf':    4,
    'abdfg':   5,
    'abdefg':  6,
    'acf':     7,
    'abcdefg': 8,
    'abcdfg':  9
}

SIGNAL = [
    #0  1  2  3  4  5  6  7  8  9 
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1], # 0 a
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 1], # 1 b
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], # 2 c
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 1], # 3 d
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0], # 4 e
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1], # 5 f
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1], # 6 g
]

SIGNAL_ORDER = [2, 5, 0, 1, 3, 4, 6]

Signal = collections.namedtuple('Signal', 'order index')

def parse_input(line):
    patterns, values = line.split(' | ')
    patterns = patterns.split()
    values = [frozenset(v) for v in values.split()]

    return patterns, values

def get_patterns(order):
    result = collections.defaultdict(str)

    st = time.time()
    for i, row in enumerate(SIGNAL):
        for j, col in enumerate(row):
            if col:
                try:
                    result[j] += order[i]
                except IndexError:
                    continue
    et = time.time()

    return {frozenset(v): k for k, v in result.items()}


def check(order, patterns, hard=False):
    result = False

    pattern_map = get_patterns(order)

    for pattern in patterns:
        for each in pattern_map:
            if hard:
                if each == pattern:
                    break
            else:
                if each.issubset(pattern):
                    break
        else:
            break
    else:
        result = True

    return result


def solve(patterns):
    patterns = {frozenset(p): p for p in patterns}

    queue = collections.deque([], 500)
    result = None
    
    letters = 'abcdefg'

    for x in letters:
        order = [''] * 7
        order[SIGNAL_ORDER[0]] = x

        queue.append(Signal(order, 0))

    letters = set(letters)

    n = 0 
    st = time.time()
    while queue:
        n += 1
        signal = queue.pop()

        if all(signal.order):
            if check(signal.order, patterns, hard=True):
                result = signal.order 
                break
        elif check(signal.order, patterns):
            idx = signal.index + 1
            for x in letters - set(signal.order):
                order = signal.order[:]
                order[SIGNAL_ORDER[idx]] = x

                queue.append(Signal(order, idx))

    et = time.time()

    # print('Took %.3f seconds to check %s patterns.' % (et - st, n))

    if not result:
        raise RuntimeError()

    return result

def main(puzzle_input, score_fn):
    n = 0

    for line in puzzle_input:
        patterns, values = parse_input(line)

        order = solve(patterns)

        pattern_values = get_patterns(order)

        n += score_fn(pattern_values, values)

    return n

def part_01(puzzle_input):
    def _score_fn(pattern_values, values):
        return sum([int(pattern_values[v]) in [1, 4, 7, 8] for v in values])

    return main(puzzle_input, _score_fn)


def part_02(puzzle_input):
    def _score_fn(pattern_values, values):
        return int(''.join(map(str, [pattern_values[v] for v in values])))

    return main(puzzle_input, _score_fn)


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
