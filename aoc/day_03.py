import collections
import json

import aoc

def bit_rate(codes, bit):
    count = collections.Counter([int(code & bit == bit) for code in codes]).most_common()

    return count[0][0], count[1][0]

def part_01(puzzle_input):
    rows = list(zip(*puzzle_input))

    gamma = []
    epsilon = []

    for row in rows:
        g, e = collections.Counter(row).most_common()

        gamma.append(g[0])
        epsilon.append(e[0])
    
    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)

    return gamma * epsilon    


def part_02(puzzle_input):
    def process(values, col, tie, idx):
        rows = list(zip(*values))

        n = (a, b) = collections.Counter(rows[col]).most_common()

        if a[1] == b[1]:
            values = [v for v in values if v[col] == tie]
        else:
            values = [v for v in values if v[col] == n[idx][0]]

        if len(values) == 1:
            return values[0]
        else:
            return process(values, col + 1, tie, idx)

    oxy = int(process(puzzle_input, 0, '1', 0), 2)
    co2 = int(process(puzzle_input, 0, '0', -1), 2)

    return oxy * co2


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
