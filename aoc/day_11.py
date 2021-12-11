import aoc


def parse(puzzle_input):
    result = {}

    for x, line in enumerate(puzzle_input):
        for y, value in enumerate(line):
            result[(x, y)] = int(value)

    return result


def adjacent(cell):
    x, y = cell

    yield x + 1, y + 1
    yield x + 1, y + 0
    yield x + 1, y - 1

    yield x + 0, y + 1
    # yield x + 0, y + 0
    yield x + 0, y - 1

    yield x - 1, y + 1
    yield x - 1, y + 0
    yield x - 1, y - 1


def compute(data):
    n = 0

    # First, the energy level of each octopus increases by 1.
    for cell in data:
        data[cell] += 1

    flashed = set()
    
    # Then, any octopus with an energy level greater than 9 flashes.
    # This increases the energy level of all adjacent octopuses by 1.
    # If this causes an octopus to have an energy level greater than 9, it also flashes. 
    # This process continues as long as new octopuses keep having their energy level increased beyond 9.
    # An octopus can only flash at most once per step.

    while True:
        flash = set()

        for cell in iter_cells(data):
            value = data[cell]

            if value <= 9:
                continue
            
            if cell in flashed:
                continue

            flash.add(cell)

            n += 1

        for cell in flash:
            for each in adjacent(cell):
                if each in data:
                    data[each] += 1

        if flash:
            flashed.update(flash)
        else:
            break

    # Finally, any octopus that flashed during this step has its energy level set to 0, 
    # as it used all of its energy to flash.
    for cell in flashed:
        data[cell] = 0

    return n


def iter_cells(data):
    max_x, max_y = max(data)

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            yield x, y


def part_01(puzzle_input):
    data = parse(puzzle_input)

    n = 0

    for i, _ in enumerate(range(100), 1):
        n += compute(data)

    return n

def part_02(puzzle_input):
    data = parse(puzzle_input)

    n = 0

    while True:
        n += 1

        if compute(data) == 100:
            break

        if n > 1000:
            break

    return n


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
