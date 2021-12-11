import aoc


def init(puzzle_input):
    values = [int(x) for x in puzzle_input[0].split(',')]

    old = [0] * 9

    for val in values:
        old[val] += 1

    return old


def main(puzzle_input, num_days):
    old = init(puzzle_input)

    for _ in range(num_days):
        new = [0] * 9

        for i, o in enumerate(old):
            if i == 0:
                new[8] += o
                new[6] += o
            else:
                new[i - 1] += o

        old = new

    return sum(old)


def part_01(puzzle_input):
    return main(puzzle_input, 80)


def part_02(puzzle_input):
    return main(puzzle_input, 256)


def cli():
    aoc.solve(__file__, part_01, part_02)

if __name__ == '__main__':
    cli()
