import pytest

from utils.file_utils import read_file
from solutions.day03 import Day03, MemoryParser, Mul

@pytest.fixture
def input_example_p1():
    return read_file("input/day03/test_input_p1.txt")

@pytest.fixture
def input_example_p2():
    return read_file("input/day03/test_input_p2.txt")

def test_p1_parse_muls(input_example_p1):
    memory_parser = MemoryParser(input_example_p1)

    muls = memory_parser.findMuls()

    assert len(muls) == 4
    assert all(isinstance(x, Mul) for x in muls) == True

def test_p1_mul():
    mul = Mul("2,2")

    assert mul.factors[0] == 2
    assert mul.factors[1] == 2
    assert mul.calculate() == 4

def test_p2_parse_muls_with_instructions(input_example_p2):
    memory_parser = MemoryParser(input_example_p2)

    muls = memory_parser.findMulsWithInstructions()

    assert len(muls) == 2
    assert all(isinstance(x, Mul) for x in muls) == True

# Example solutions
def test_p1_solution(input_example_p1):
    day03 = Day03(input_example_p1)

    assert day03.part1_solution() == 161

def test_p2_solution(input_example_p2):
    day03 = Day03(input_example_p2)

    assert day03.part2_solution() == 48