import collections
import itertools

import aoc

ScannerData = collections.namedtuple('ScannerData', 'id points')
Point3d = collections.namedtuple('Point3d', 'x,y,z')


def parse(puzzle_input):
    index = -1
    points = []

    for line in puzzle_input:
        if 'scanner' in line:
            index += 1
            points = []
            continue

        if line:
            points.append(Point3d(*eval(line)))
        else:
            yield ScannerData(index, points) 

    yield ScannerData(index, points) 


def point_to_point_vectors(scanner_data):
    result = collections.defaultdict(set)

    for a in scanner_data.points:
        for b in scanner_data.points:
            x = sum(
                [
                    pow(b.x - a.x, 2),
                    pow(b.y - a.y, 2),
                    pow(b.z - a.z, 2),
                ]
            )

            result[a].add(x)
            result[b].add(x)
    
    return result


def pstr(p):
    return '{},{},{}'.format(*p)


def shared_points(sa, sb, ptpvs):
    result = set()

    for pa in sa.points:
        for pb in sb.points:
            match = ptpvs[sa.id][pa] & ptpvs[sb.id][pb]

            if len(match) == 12:
                result.add(((sa.id, pa), (sb.id, pb)))
                break

    return result


def part_01(puzzle_input):
    scans = list(parse(puzzle_input))
    ptpvs = {scan.id: point_to_point_vectors(scan) for scan in scans}

    print()

    count = collections.Counter()
    n = 0

    for sa, sb in itertools.combinations(scans, 2):
        p = shared_points(sa, sb, ptpvs)

        for (ia, pa), (ib, pb) in p:
            count[(ia, pa)] += 1
            count[(ib, pb)] += 1


def part_02(puzzle_input):
    return None


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
