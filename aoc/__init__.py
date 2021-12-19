import time
import os


def puzzle_input(day, source='data'):
    day, _ = os.path.splitext(os.path.basename(day))
    day = day[:6]

    path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..', source, '{}.txt'.format(day)
        )
    )

    with open(path, 'r') as fp:
        return [line.strip() for line in fp.readlines()]


def solve(day, fn_01, fn_02):
    args = puzzle_input(day)
    
    st = time.time()
    answer_01 = fn_01(args)
    print(f'Part 01: {answer_01}')
    et = time.time()
    print("Took {:.3f} seconds".format(et - st))

    st = time.time()
    answer_02 = fn_02(args)
    print(f'Part 02: {answer_02}')
    et = time.time()
    print("Took {:.3f} seconds".format(et - st))