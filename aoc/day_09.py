import collections
import functools
import operator

import aoc

def parse_input(puzzle_input):
    result = {}

    for col, line in enumerate(puzzle_input):
        for row, ch in enumerate(line):
            result[(row, col)] = int(ch)
    
    return result

def adjcent(cell):
    x, y = cell 

    yield (x - 1, y + 0) 
    yield (x + 1, y + 0) 
    yield (x + 0, y - 1)
    yield (x + 0, y + 1)


def is_lowest_in_area(cell, cells):
    result = [False, False, False, False]

    n = cells[cell]

    for i, each in enumerate(adjcent(cell)):
        x = cells.get(each)

        if x is None or x > n:
            result[i] = True
    
    return all(result)


def part_01(puzzle_input):
    cells = parse_input(puzzle_input)
    
    risk = 0

    for cell, height in cells.items():
        if is_lowest_in_area(cell, cells):
            risk += (height + 1)

    return risk


def get_basin(start, cells):
    queue = collections.deque()
    queue.append(start)

    basin = set()

    while True:
        try:
            cell = queue.popleft()
        except IndexError:
            break

        try:
            height = cells[cell]
        except KeyError:
            continue

        if height == 9:
            continue

        if cell in basin:
            continue

        basin.add(cell)

        for each in adjcent(cell):
            queue.append(each)

    return basin


def part_02(puzzle_input):
    cells = parse_input(puzzle_input)

    basins = []

    visited = set()

    for cell, height in cells.items():
        if cell in visited:
            continue

        if height == 9:
            continue

        basin = get_basin(cell, cells)

        visited.update(basin)

        basins.append(len(basin))

    basins = sorted(basins)

    return functools.reduce(operator.mul, basins[-3:])
        

def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
