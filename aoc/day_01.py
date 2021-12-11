import itertools

import aoc


def main(puzzle_input, chunk_size):
    puzzle_input = [int(x) for x in puzzle_input]
    
    def iter_chunks(n):
        s = slice(None, -(n-1) or None)

        for i, _ in enumerate(puzzle_input[s]):
            yield sum(itertools.islice(puzzle_input, i, i + n))

    prev = itertools.islice(iter_chunks(chunk_size), 0, None)
    curr = itertools.islice(iter_chunks(chunk_size), 1, None)

    return sum([int(b > a) for a, b in zip(prev, curr)])


def part_01(puzzle_input):
    return main(puzzle_input, 1)


def part_02(puzzle_input):
    return main(puzzle_input, 3)


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
