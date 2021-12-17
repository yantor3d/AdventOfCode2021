import collections
import itertools
import re

import aoc

Point = collections.namedtuple('Point', 'x y')
Area = collections.namedtuple('Area', 'min max')


def parse(puzzle_input):
    match = re.match(r'.*: x=(.*), y=(.*)', puzzle_input[0])

    x_min, x_max = match.groups()[0].split('..')
    y_min, y_max = match.groups()[1].split('..')

    return Area(
        Point(int(x_min), int(y_min)),
        Point(int(x_max), int(y_max)),
    )


def solve(dx, dy, area):
    x, y = 0, 0

    hit = False

    while True:
        x += dx
        y += dy

        if dx > 0:
            dx -= 1
        if dx < 0:
            dx += 1 

        dy -= 1

        if x > area.max.x:
            break

        if y < area.min.y:
            break
    
        if (x >= area.min.x and x <= area.max.x) and (y >= area.min.y and y <= area.max.y):
            hit = True 
            break

    return hit


def sum_range(n):
    if n % 2:
        return int(n * ((n + 1) / 2))
    else:
        return int((n + 1) * (n / 2))


def main(puzzle_input):
    area = parse(puzzle_input)

    x_values = range(1, area.max.x + 1)
    y_values = range(area.min.y * -1 + 1, area.min.y - 1, -1)

    hits = []

    for x, y in itertools.product(x_values, y_values):
        if solve(x, y, area):
            hits.append((x, y))

    return hits


def part_01(puzzle_input):
    return max(sum_range(y) for _, y in main(puzzle_input))


def part_02(puzzle_input):
    return len(main(puzzle_input))


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
