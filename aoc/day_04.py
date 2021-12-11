import aoc

class Board(object):
    def __init__(self, values, row_count, col_count):
        self.values = values 
        self.row_count = row_count
        self.col_count = col_count

        self.playing = True
        self.called = set()

    def __str__(self):
        lines = [
            ' '.join(['{:>2d}'.format(x) for x in row])
            for row in self.rows()
        ]

        return '\n'.join(lines)

    def __repr__(self):
        return "{}({}, {}, {})".format(
            self.__class__.__name__,
            self.values,
            self.row_count,
            self.col_count,
        )

    def rows(self):
        for x in range(self.row_count):
            yield self.row(x)

    def cols(self):
        for x in range(self.col_count):
            yield self.col(x)

    def row(self, n):
        return [self.values[(n * self.row_count) + i] for i in range(self.col_count)]

    def col(self, n):
        return [self.values[n + (i * self.col_count)] for i in range(self.row_count)]

    def check(self, n):
        if not self.playing:
            return False

        self.called.add(n)

        for row in self.rows():
            if set(row).issubset(self.called):
                return True
        
        for col in self.cols():
            if set(col).issubset(self.called):
                return True
        
        return False

    def score(self, n):
        self.playing = False

        return sum(set(self.values) - self.called) * n


def parse(puzzle_input):
    lines = iter(puzzle_input)

    numbers = [int(x) for x in next(lines).split(',')]

    next(lines)

    boards = []

    values = iter(' '.join(lines).split())

    while True:
        try:
            boards.append(Board([int(next(values)) for _ in range(25)], 5, 5))
        except StopIteration:
            break

    return numbers, boards


def main(puzzle_input):
    numbers, boards = parse(puzzle_input)

    results = []

    for n in numbers:
        for board in boards:
            if board.check(n):
                results.append(board.score(n))

    return results


def part_01(puzzle_input):
    return main(puzzle_input)[0]


def part_02(puzzle_input):
    return main(puzzle_input)[-1]


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
