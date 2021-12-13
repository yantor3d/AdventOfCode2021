import collections

import aoc

Point = collections.namedtuple('Point', 'x y')


def parse(puzzle_input):
    data = set()
    folds = []

    lines = iter(list(puzzle_input))

    for line in lines:
        if not line:
            break

        x, y = line.split(',')

        data.add(Point(int(x), int(y)))
    
    for line in lines:
        cmd = line.rsplit(' ')[-1]

        axis, v = cmd.split('=')

        if axis == 'x':
            folds.append(Point(int(v), 0))
        elif axis == 'y':
            folds.append(Point(0, int(v)))

    return data, folds


def fold(data, at):
    result = set()

    # THIS IS NOT RIGHT
    for old in data:
        # Fold -X -> +X
        if at.y == 0:
            if old.x > at.x:
                new = Point(at.x - (old.x - at.x), old.y)
            else:
                new = old

        # Fold -Y -> +Y
        elif at.x == 0:
            if old.y > at.y:
                new = Point(old.x, at.y - (old.y - at.y))
            else:
                new = old
        
        result.add(new)
    
    return result


def part_01(puzzle_input):
    data, folds = parse(puzzle_input)

    for f in folds:
        data = fold(data, f)
        break

    return len(data)


def pprint(data, f=None):
    x = -1
    y = -1

    for p in data:
        x = max(x, p.x)
        y = max(y, p.y)

    lines = [['.'] * (x + 1) for _ in range(y + 1)]

    for p in data:
        lines[p.y][p.x] = '#'

    if f is not None:
        if f.x == 0:
            for x in range(x + 1):
                lines[f.y][x] = '='

        if f.y == 0:
            for y in range(y + 1):
                lines[y][f.x] = '|'

    lines = [''.join(line) for line in lines]
    lines = '\n'.join(lines)

    return lines


def part_02(puzzle_input):
    data, folds = parse(puzzle_input)
    
    for f in folds:
        data = fold(data, f)


    return '\n' + pprint(data)


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
