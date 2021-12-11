import collections

import aoc

TOKENS = ['{}', '<>', '[]', '()']
TOKEN_PAIRS = {}

TOKEN_PAIRS.update({k: v for k, v in TOKENS})
TOKEN_PAIRS.update({v: k for k, v in TOKENS})

OPEN, CLOSE = list(zip(*TOKENS))

EXTRA_COST = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

SYNTAX_COST = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def parse_line(line):
    ptr = 0
    stack = []

    for i, token in enumerate(line):
        ptr = i
    
        if token in OPEN:
            stack.append(token)
        if token in CLOSE:
            out = TOKEN_PAIRS[token]
            top = stack.pop(-1)
            
            if out == top:
                continue

            # print("%s - Expected %s, but found %s instead - %s." % (line, TOKEN_PAIRS[top], token, line[ptr]))
            
            break
    else:
        ptr = -1 

    # if stack and ptr == -1:
    #     print("%s - Encountered unexpected end of line - %s" % (line, ''.join(stack)))

    return stack, ptr


def part_01(puzzle_input):
    n = 0

    # print()

    for line in puzzle_input:
        stack, ptr = parse_line(line)

        if ptr == -1:
            continue 

        n += SYNTAX_COST[line[ptr]]

    return n


def part_02(puzzle_input):
    scores = []

    for line in puzzle_input:
        stack, ptr = parse_line(line)

        if ptr != -1:
            continue 

        end_of_line = ''.join(TOKEN_PAIRS[x] for x in stack[::-1])

        # print('%s - Complete by adding %s' % (line, end_of_line))

        scores.append(score_auto_complete(end_of_line))

    scores.sort()

    n = int(len(scores) / 2)

    return scores[n]


def score_auto_complete(tail):
    n = 0 

    for x in tail:
        n *= 5
        n += EXTRA_COST[x]

    return n


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
