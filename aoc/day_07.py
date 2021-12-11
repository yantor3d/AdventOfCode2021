import collections
import enum
import functools
import math
import sys

import aoc


def main(puzzle_input, cost_fn=None):
    cost_fn = cost_fn or linear_cost

    values = [int(x) for x in puzzle_input[0].split(',')]

    positions = [0] * (max(values) + 1)

    for val in values:
        for i, _ in enumerate(positions):
            positions[i] += cost_fn(val, i)

    return positions


def linear_cost(old, new):
    return abs(old - new)


def culmulative_cost(old, new):
    d = abs(old - new)

    return int(((d * d) + d) / 2)


def part_01(puzzle_input):
    return min(main(puzzle_input, linear_cost))


def part_02(puzzle_input):
    return min(main(puzzle_input, culmulative_cost))


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
