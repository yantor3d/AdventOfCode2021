import math
import collections
import itertools

import aoc


def parse(puzzle_input):
    lines = iter(puzzle_input)

    data = next(lines)
    rules = {}

    next(lines)

    for line in lines:
        old, add = line.split(' -> ')

        rules[old] = (old[0] + add, add + old[1])

    data = [data[i] + data[i + 1] for i, _ in enumerate(data[:-1])]
    data = collections.Counter(data)

    return data, rules


def solve(data, rules):
    result = collections.Counter(data)
    update = collections.Counter()

    for old, num in result.items():
        a, b = rules[old]

        update[old] -= num
        update[a] += num
        update[b] += num

    for k, v in update.items():
        result[k] += v 

    result = {k: v for k, v in result.items() if v}

    return result


def count(data):
    result = collections.Counter()

    for (a, b), v in data.items():
        # Only count each letter once
        # result[a] += v 
        result[b] += v

    return result


def main(puzzle_input, n):
    data, rules = parse(puzzle_input)

    for _ in range(n):
        data = solve(data, rules)

    result = count(data).most_common()

    return result[0][1] - result[-1][1]

def part_01(puzzle_input):
    return main(puzzle_input, 10)


def part_02(puzzle_input):
    return main(puzzle_input, 40)


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
