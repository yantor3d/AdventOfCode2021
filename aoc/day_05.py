import collections
import itertools
import operator

import aoc

class Point(collections.namedtuple('Point', 'x y')):
    @classmethod
    def from_str(cls, text):
        x, y = text.split(',')

        return cls(int(x), int(y))


class LineSegment(collections.namedtuple('LineSegment', 'start end')):
    @classmethod
    def from_str(cls, text):
        start, end = text.split(' -> ')
    
        return cls(
            Point.from_str(start),
            Point.from_str(end)
        )

    def is_orthogonal(self):
        return (self.start.x == self.end.x or self.start.y == self.end.y)

    def delta(self, value):
        if value > 0:
            return 1
        elif value < 0:
            return -1
        else:
            return 0

    def points(self):
        d = Point(
            self.delta(self.end.x - self.start.x),
            self.delta(self.end.y - self.start.y)
        )

        p = self.start

        while True:
            yield p

            if p == self.end:
                break

            p = Point(p.x + d.x, p.y + d.y)


def parse(puzzle_input):
    for line in puzzle_input:
        yield LineSegment.from_str(line)


def main(puzzle_input, predicate):
    data = list(parse(puzzle_input))

    vents = collections.Counter(
        itertools.chain.from_iterable(
            [
                ls.points() for ls in data if predicate(ls)
            ]
        )
    )
    
    result = sum([int(n > 1) for p, n in vents.items()])

    return result


def part_01(puzzle_input):
    return main(puzzle_input, operator.methodcaller('is_orthogonal'))


def part_02(puzzle_input):
    return main(puzzle_input, lambda x: True)


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
