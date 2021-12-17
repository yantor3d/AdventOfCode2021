import collections
import functools
import operator
import aoc

Packet = collections.namedtuple('Packet', 'version type_id payload')

HEX_TO_BIN = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

class ByteStream(object):
    def __init__(self, data):
        self.data = data
        self.ptr = 0
        self.eof = len(data)

    def __call__(self, n):
        result = self.data[self.ptr:self.ptr + n]

        self.ptr += n

        return result


def literal(stream):
    result = ''

    while True:
        block = stream(5)

        result += block[1:]

        if block[0] == '0':
            break
    
    return int(result, 2)

def op(stream):
    payload = []

    op_type_id = stream(1)

    if op_type_id == '0':
        sub_packet_len = int(stream(15), 2)
        s = stream.ptr 

        while True:
            payload.append(parse(stream))
    
            if stream.ptr >= s + sub_packet_len:
                break
    else:
        sub_packet_num = int(stream(11), 2)

        for _ in range(sub_packet_num):
            payload.append(parse(stream))

    return payload


def parse(stream, n=0):
    packet_version = int(stream(3), 2)
    packet_type_id = int(stream(3), 2)

    if packet_type_id == 4:
        payload = [literal(stream)]
    else:
        payload = op(stream)

    result = Packet(packet_version, packet_type_id, payload) 

    return result

def test(data):
    return parse(ByteStream(data))


def unpack(packet):
    yield packet

    for each in packet.payload:
        if isinstance(each, Packet):
            yield from unpack(each)


def hex_to_bin(hex):
    result = ''

    for each in hex:
        result += HEX_TO_BIN[each]

    return result

def part_01(puzzle_input):
    data = hex_to_bin(puzzle_input[0])

    result = 0

    packets = parse(ByteStream(data))

    for each in unpack(packets):
        result += each.version

    return result


def sum_(packet):
    return sum([solve(p) for p in packet.payload])


def product(packet):
    return functools.reduce(operator.mul, [solve(p) for p in packet.payload])


def min_(packet):
    return min([solve(p) for p in packet.payload])


def max_(packet):
    return max([solve(p) for p in packet.payload])


def greater_than(packet):
    return int(solve(packet.payload[0]) > solve(packet.payload[1]))



def less_than(packet):
    return int(solve(packet.payload[0]) < solve(packet.payload[1]))


def equal_to(packet):
    return int(solve(packet.payload[0]) == solve(packet.payload[1]))


def value_of(packet):
    return packet.payload[0]


def solve(packet):

    operators = {
        0: sum_,
        1: product,
        2: min_,
        3: max_,
        4: value_of,
        5: greater_than,
        6: less_than,
        7: equal_to,
    }

    op = operators[packet.type_id]

    return op(packet)


def part_02(puzzle_input):
    data = hex_to_bin(puzzle_input[0])

    packet = parse(ByteStream(data))   
    result = solve(packet)

    return result


def cli():
    aoc.solve(__file__, part_01, part_02)


if __name__ == '__main__':
    cli()
