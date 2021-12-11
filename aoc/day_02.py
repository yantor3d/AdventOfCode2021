import collections

import aoc

Move = collections.namedtuple('Move', 'aim x y')

class Direction(object):
    FD = 'forward'
    DN = 'down'
    UP = 'up'
 

def parse(command):
     direction, value = command.split()

     return direction, int(value)


def main(puzzle_input, op):
    a, x, y = 0, 0, 0

    for each in puzzle_input:
        d, v = parse(each)

        a, x, y = op(a, x, y, d, v)
    
    return x * y

def part_01(puzzle_input):
    def op(a, x, y, d, v):
        return {
            Direction.DN: (a, x + 0, y + v),
            Direction.FD: (a, x + v, y + 0),
            Direction.UP: (a, x + 0, y - v),
        }[d]

    return main(puzzle_input, op)


def part_02(puzzle_input):
    def op(a, x, y, d, v):
        return {
            Direction.DN: (a + v, x + 0, y + 0),
            Direction.FD: (a + 0, x + v, y + (a * v)),
            Direction.UP: (a - v, x + 0, y + 0),
        }[d]

    return main(puzzle_input, op)


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
