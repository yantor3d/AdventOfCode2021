import string 
import collections
import sys
import heapq

import aoc


def parse(puzzle_input):
    result = {}

    for y, line in enumerate(puzzle_input):
        for x, each in enumerate(line): 
            result[x, y] = int(each)

    return result


def extend(data):
    result = {}

    mx, my = max(data)
    mx += 1
    my += 1

    for x in range(mx * 5):
        for y in range(my * 5):
            result[x, y] = '.'

    for dx in range(5):
        for dy in range(5):
            for (x, y), value in sorted(data.items()):
                nx = (mx * dx + x)
                ny = (my * dy + y)

                v = value + dx + dy

                if v > 9:
                    v -= 9

                result[nx, ny] = v

    return result


def adjacent(cell):
    x, y = cell

    yield x + 0, y + 1 
    yield x + 0, y - 1

    yield x + 1, y + 0
    yield x - 1, y + 0
    

def solve(data):
    start = min(data)
    stop = max(data)

    previous_nodes = {}

    distances = {}
    distances[start] = 0

    queue = []
    queue.append([0, start])

    heapq.heapify(queue)

    while queue:
        priority, node = heapq.heappop(queue)

        if node == stop:
            break

        for each in adjacent(node):
            if each not in data:
                continue

            dist = distances[node] + data[each]
            
            if distances.get(each, sys.maxsize) > dist:
                distances[each] = dist
                priority = dist + (abs(each[0] - stop[0]) + abs(each[1] + stop[1]))

                heapq.heappush(queue, (priority, each))

    return distances[stop]


def main(data):
    path, cost = solve(data)

    start = min(data)
    stop = max(data)

    result = []
    node = stop

    n = 0

    while node != start:
        n += data[node]

        result.append(node)
        node = path[node]

    return n


def part_01(puzzle_input):
    data = parse(puzzle_input)

    return solve(data)

def part_02(puzzle_input):
    data = parse(puzzle_input)
    data = extend(data)

    return solve(data)


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
