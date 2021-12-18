import pytest 

import aoc.day_18 as solve

@pytest.fixture(scope='module')
def puzzle_input():
    return [
        '[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]',
        '[[[5,[2,8]],4],[5,[[9,9],0]]]',
        '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]',
        '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]',
        '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]',
        '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]',
        '[[[[5,4],[7,7]],8],[[8,3],8]]',
        '[[9,3],[[9,9],[6,[4,9]]]]',
        '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]',
        '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]',
    ]


def test_add():
    a = [1, 2]
    b = [[3, 4], 5]

    x = solve.add(a, b)

    assert x == [[1, 2], [[3, 4], 5]]

@pytest.mark.parametrize(
    'number,answer',
    (
        (10, [5, 5]),
        (11, [5, 6]),
        (12, [6, 6]),
    )
)
def test_split_value(number, answer):
    assert solve.split(number) == answer


@pytest.mark.parametrize(
    'number',
    (
        [1,2],
        [[1,2],3],
        [9,[8,7]],
        [[1,9],[8,5]],
        [[[[1,2],[3,4]],[[5,6],[7,8]]],9],
        [[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]],
        [[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]],
    )
)
def test_snail_number(number):
    snail = solve.SnailNumber.from_list(number)
    assert snail.as_list() == number


@pytest.mark.parametrize(
    'number,answer',
    (
        ([[[[[9,8],1],2],3],4], [9, 8]),
        ([7,[6,[5,[4,[3,2]]]]], [3, 2]),
        ([[6,[5,[4,[3,2]]]],1], [3, 2]),
        ([[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], [7, 3]]),
        ([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], [3, 2]),
        ([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]], [6,7]),
    )
)
def test_explodable(number, answer):
    snail = solve.SnailNumber.from_list(number)

    assert snail.explodable().as_list() == answer


@pytest.mark.parametrize(
    'number,answer',
    (
        ([[[[[9,8],1],2],3],4], [[[[0,9],2],3],4]),
        ([7,[6,[5,[4,[3,2]]]]], [7,[6,[5,[7,0]]]]),
        ([[6,[5,[4,[3,2]]]],1], [[6,[5,[7,0]]],3]),
        ([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]),
        ([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[7,0]]]]),
    )
)
def test_explode(number, answer):
    snail = solve.SnailNumber.from_list(number)

    assert snail.explode()
    assert snail.as_list() == answer


@pytest.mark.parametrize(
    'number,answer',
    (
        ([0, 10], [0, 10]),
        ([[[[0,7],4],[15,[0,13]]],[1,1]], [15,[0,13]]), 
        ([[[[0,7],4],[[7,8],[0,13]]],[1,1]], [0,13]),
    )
)
def test_splittable(number, answer):
    snail = solve.SnailNumber.from_list(number)

    assert snail.splittable().as_list() == answer


@pytest.mark.parametrize(
    'number,answer',
    (
        ([[[[0,7],4],[15,[0,13]]],[1,1]], [[[[0,7],4],[[7,8],[0,13]]],[1,1]]),
        ([[[[0,7],4],[[7,8],[0,13]]],[1,1]], [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])
    )
)
def test_split(number, answer):
    snail = solve.SnailNumber.from_list(number)

    assert snail.split()
    assert snail.as_list() == answer


def test_example():
    snail = solve.SnailNumber.from_list([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])
    
    assert snail.explode()
    assert snail.as_list() == [[[[0,7],4],[7,[[8,4],9]]],[1,1]]

    assert snail.explode()
    assert snail.as_list() == [[[[0,7],4],[15,[0,13]]],[1,1]]

    assert snail.split()
    assert snail.as_list() == [[[[0,7],4],[[7,8],[0,13]]],[1,1]]

    assert snail.split()
    assert snail.as_list() == [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]

    assert snail.explode()
    assert snail.as_list() == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]

    assert snail.explodable() is None
    assert snail.splittable() is None


def test_solve():
    snail = solve.SnailNumber.from_list([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])
    snail.solve()

    assert snail.as_list() == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]

@pytest.mark.parametrize(
    'number,answer',
    (
        ([9,1], 29),
        ([[9,1],[1,9]], 129),
        ([[1,2],[[3,4],5]], 143),
        ([[[[0,7],4],[[7,8],[6,0]]],[8,1]], 1384),
        ([[[[1,1],[2,2]],[3,3]],[4,4]], 445),
        ([[[[3,0],[5,3]],[4,4]],[5,5]], 791),
        ([[[[5,0],[7,4]],[5,5]],[6,6]], 1137),
        ([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]], 3488),
    )
)
def test_score(number, answer):
    snail = solve.SnailNumber.from_list(number)

    assert snail.magnitude() == answer


def test_part_01(puzzle_input):
    assert solve.part_01(puzzle_input) == 4140


def test_part_02(puzzle_input):
    assert solve.part_02(puzzle_input) == 3993
