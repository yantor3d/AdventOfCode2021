import pytest 

import aoc.day_16 as solve

@pytest.fixture(scope='module')
def puzzle_input():
    return [
    ]

@pytest.mark.skip
@pytest.mark.parametrize(
    'puzzle_input,answer',
    (
        ('110100101111111000101000', [2021]),
        ('00111000000000000110111101000101001010010001001000000000', [10, 20]),
        ('11101110000000001101010000001100100000100011000001100000', [1, 2, 3]),
    )
)
def test_binary_examples(puzzle_input, answer):
    packet = solve.test(puzzle_input)
    result = []

    for each in solve.unpack(packet):
        for val in each.payload:
            if isinstance(val, int):
                result.append(val)

    assert result == answer


@pytest.mark.parametrize(
    'puzzle_input,answer',
    (
        (['8A004A801A8002F478'], 16),
        (['620080001611562C8802118E34'], 12),
        (['C0015000016115A2E0802F182340'], 23),
        (['A0016C880162017C3686B18A3D4780'], 31),
    )
)
def test_part_01(puzzle_input, answer):
    assert solve.part_01(puzzle_input) == answer


@pytest.mark.parametrize(
    'puzzle_input,answer',
    (
        (['C200B40A82'], 3),
        (['04005AC33890'], 54),
        (['880086C3E88112'], 7),
        (['CE00C43D881120'], 9),
        (['D8005AC2A8F0'], 1),
        (['F600BC2D8F'], 0),
        (['9C005AC2F8F0'], 0),
        (['9C0141080250320F1802104A08'], 1),
    )
)
def test_part_02(puzzle_input,answer):
    assert solve.part_02(puzzle_input) == answer
