import collections

import aoc


def parse(puzzle_input):
    data = collections.defaultdict(set)

    for line in puzzle_input:
        a, b = line.split('-')

        data[a].add(b)
        data[b].add(a)

    return data

def solve(puzzle_input, can_visit):
    paths = []

    data = parse(puzzle_input)

    search = collections.deque()
    search.append(['start',])

    while search:
        path = search.popleft()

        tail = path[-1]

        for next_ in data[tail]:
            if next_ == 'start':
                continue

            if next_ == 'end':
                paths.append(path[:] + [next_])
                continue

            if can_visit(path, next_):
                search.append(path[:] + [next_])

    return paths


def part_01(puzzle_input):
    def can_visit(path, next_):
        if str.islower(next_) and next_ in path:
            return False

        return True

    paths = solve(puzzle_input, can_visit)

    return len(paths)


def part_02(puzzle_input):
    def can_visit(path, next_):
        if str.islower(next_):
            small_caves_visited = [path.count(each) for each in path if str.islower(each)]

            if next_ in path and 2 in small_caves_visited:
                return False

        return True

    paths = solve(puzzle_input, can_visit)

    return len(paths)


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
