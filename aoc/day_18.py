import functools
import math
import itertools

import aoc

class Root(object):
    a = 0
    b = 0
    depth = 0


class SnailNumber(object):
    def __init__(self, a, b):
        self.parent = Root()
        self.a = a if isinstance(a, int) else SnailNumber.from_list(a)
        self.b = b if isinstance(b, int) else SnailNumber.from_list(b)

        if isinstance(self.a, SnailNumber):
            self.a.parent = self

        if isinstance(self.b, SnailNumber):
            self.b.parent = self

    def __repr__(self):
        a, b = self.as_list()

        return '{}(a={}, b={})'.format(self.__class__.__name__, a, b)

    def __iter__(self):
        if isinstance(self.a, SnailNumber):
            yield from self.a

        yield self

        if isinstance(self.b, SnailNumber):
            yield from self.b

    def as_list(self):
        return [
            self.a if isinstance(self.a, int) else self.a.as_list(),
            self.b if isinstance(self.b, int) else self.b.as_list(),
        ]

    @classmethod
    def from_list(cls, lst):
        return cls(*lst)

    @property
    def root(self):
        result = self

        while True:
            if isinstance(result.parent, SnailNumber):
                result = result.parent
            else:
                break
        
        return result

    @property
    def depth(self):
        return 1 + self.parent.depth

    def explodable(self):
        for pair in self:
            if pair.parent.depth == 4:
                return pair

    def explode(self):
        result = True

        for pair in self:
            if pair.parent.depth < 4:
                continue

            pair.__explode()
            break
        else:
            result = False
        
        return result
                
    def __explode(self):
        nodes = list(self.root)

        for node in reversed(nodes[:nodes.index(self)]):
            if isinstance(node.b, int):
                node.b += self.a
                break

            if isinstance(node.a, int):
                node.a += self.a
                break

        for node in nodes[nodes.index(self) + 1:]:
            if isinstance(node.a, int):
                node.a += self.b
                break

            if isinstance(node.b, int):
                node.b += self.b
                break

        if self.parent.a == self:
            self.parent.a = 0

        if self.parent.b == self:
            self.parent.b = 0

    def splittable(self):
        for pair in self:
            if isinstance(pair.a, int) and pair.a > 9:
                return pair 
                
            if isinstance(pair.b, int) and pair.b > 9:
                return pair 

    def split(self):
        result = True

        for pair in self:
            if isinstance(pair.a, int) and pair.a > 9:
                pair.a = self.__split(pair.a, pair)
                break

            if isinstance(pair.b, int) and pair.b > 9:
                pair.b = self.__split(pair.b, pair)
                break
        else:
            result = False

        return result

    def __split(self, n, parent):
        result = SnailNumber.from_list(split(n))
        result.parent = parent

        return result 

    def magnitude(self):
        if isinstance(self.a, int):
            a = self.a
        else:
            a = self.a.magnitude()

        if isinstance(self.b, int):
            b = self.b
        else:
            b = self.b.magnitude()
        
        return (a * 3) + (b * 2)

    def solve(self):
        n = 0 
        while True:
            n += 1

            if n > 1000:
                raise RuntimeError("Something is wrong")

            if self.explode():
                continue 

            if self.split():
                continue

            break
        return self


def add(a, b):
    """To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. 
    
    For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]
    """

    return SnailNumber.from_list([a, b]).solve().as_list()



def split(number):
    return [
        math.floor(number / 2),
        math.ceil(number / 2)
    ]


def parse(puzzle_input):
    return [eval(line) for line in puzzle_input]


def part_01(puzzle_input):
    data = parse(puzzle_input)

    result = functools.reduce(add, data)

    return SnailNumber.from_list(result).magnitude()


def part_02(puzzle_input):
    data = parse(puzzle_input)

    result = [
        SnailNumber.from_list(add(a, b)).magnitude()
        for a, b in itertools.permutations(data, 2)
    ]

    return max(result)


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
