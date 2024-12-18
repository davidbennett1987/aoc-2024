import pytest

from utils.file_utils import read_file
from solutions.day04 import Cell, Day04, Grid, LineReader, XMAS_Counter

@pytest.fixture
def input_example():
    return read_file("input/day04/test_input.txt")

def test_p1_horizontals(input_example):
    grid = Grid(str.splitlines(input_example))
    horizontals = grid.rows

    assert len(horizontals) == 10
    assert LineReader.read(horizontals[0]) == "MMMSXXMASM"
    assert LineReader.read(horizontals[9]) == "MXMXAXMASX"

def test_p1_verticals(input_example):
    grid = Grid(str.splitlines(input_example))
    verticals = grid.columns

    assert len(verticals) == 10
    assert LineReader.read(verticals[0]) == "MMAMXXSSMM"
    assert LineReader.read(verticals[9]) == "MAMXMASAMX"

def test_p1_diagonals(input_example):
    grid = Grid(str.splitlines(input_example))
    diagonals = grid.diagonals

    assert len(diagonals) == 38
    assert LineReader.read(diagonals[0]) == "M"
    assert LineReader.read(diagonals[2]) == "ASM"
    assert LineReader.read(diagonals[9]) == "MAXMMMMASM"
    assert LineReader.read(diagonals[16]) == "AMA"
    assert LineReader.read(diagonals[18]) == "X"
    assert LineReader.read(diagonals[27]) == "MMASMASMS"
    assert LineReader.read(diagonals[37]) == "M"

def test_p1_xmas_counter():
    assert XMAS_Counter.count([[]]) == 0
    assert XMAS_Counter.count([[
        Cell("M", 0, 0),
        Cell("A", 0, 0),
        Cell("M", 0, 0),
        Cell("X", 0, 0),
        Cell("M", 0, 0),
        Cell("A", 0, 0),
        Cell("S", 0, 0),
        Cell("A", 0, 0),
        Cell("M", 0, 0),
        Cell("X", 0, 0)
    ]]) == 2
    assert XMAS_Counter.count([[
        Cell("X", 0, 0),
        Cell("M", 0, 0),
        Cell("A", 0, 0),
        Cell("S", 0, 0),
        Cell("X", 0, 0)
    ]]) == 1
    assert XMAS_Counter.count([[
        Cell("X", 0, 0),
        Cell("M", 0, 0),
        Cell("A", 0, 0),
        Cell("S", 0, 0),
        Cell("S", 0, 0),
        Cell("A", 0, 0),
        Cell("M", 0, 0),
        Cell("X", 0, 0)
    ]]) == 2

# Example solutions
def test_p1_solution(input_example):
    day04 = Day04(input_example)

    assert day04.part1_solution() == 18

def test_p2_solution(input_example):
    day04 = Day04(input_example)

    assert day04.part2_solution() == 9